#
# 
# Authors: Christian Schuler & Dominik Hauser
################################################################################

import ffmpeg
import os.path as path
from moviepy.editor import *
import re
import argparse
import textgrid
import numpy as np
import imageio
#from PIL import Image



class editing():
    
    def __init__(self, path_to_file, path_to_save):
        self.path_to_file = path_to_file
        self.path_to_save = path_to_save
        
        self.clip, self.type = self.getClipFromPath(path_to_file)
        self.clip_history = []
        
    def getClipFromPath(self, path_to_file):
        try:
            return VideoFileClip(path_to_file), "video"
        except:
            pass
        
        try:
            return AudioFileClip(path_to_file), "audio"
        except:
            raise Exception('File is neither a video nor an audio file.')
    
   
    #Manages the clip history and ensures that no more than 5 copies are saved
    def _clipHistory(self):
        self.clip_history.append(self.clip.copy())
        if len(self.clip_history) >5:
            self.clip_history.remove(0)
    
    def getClip(self):
        return self.clip
        
    def getAudioClip(self):
        return self.clip.audio    
        
    def setAudioClip(self, audio_clip):
        self._clipHistory()
        self.clip.set_audio(audio_clip)
        return self.clip

    """
    Functions for sorting by numbers. Remove anything than the numbers in a string.
    """
    def atoi(self, text):
        return int(text) if text.isdigit() else text

    def natural_keys(self, text):
        return [ self.atoi(c) for c in re.split(r'(\d+)', text) ]    
    
    #Stores the last 5 clips
    def undo():
        if len(self.clip_history) >0:
            self.clip = self.clip_history[-1]
            del self.clip_history[-1]
        

    #Creates DIR when not existent
    def checkDirExistsAndCreate(self, pathToCheck):
        if not os.path.exists(pathToCheck):
            os.makedirs(pathToCheck)
     
        

    def cut(self, start, end):
        self._clipHistory()
        if start < 0:
            start = 0
        if end < 0 or end > self.clip.duration:
            end = self.clip.duration
        
        self.clip.subclip(start, end)
        return self.clip
    
    

    def get_frame(self, frame_time):
        return self.clip.get_frame(frame_time)

    def save_frame(self, frame_time, frame_name, extension = 'png'):
        imageio.imwrite(self.path_to_save + frame_name  + '.' + extension, self.get_frame(frame_time))



    def save_all_frames(self, path_optional = '', extension = 'png'):
        if self.type == 'video':
            fps = self.clip.fps
            numberOfFrames = int(fps * self.clip.duration)
            path = self.path_to_save if path_optional =='' else path_optional
            self.checkDirExistsAndCreate(path)
            for f in range(numberOfFrames):
                frame = self.clip.get_frame(f*1.0/fps)
                normalized_array = (frame - np.min(frame)) / (np.max(frame) - np.min(frame))
                img = (normalized_array * 255).astype(np.uint8)
                imageio.imwrite(path + 'frame'+ str(f) + '.' + extension, img)
        

    def remove_frame_time(self, frame_time):
        self._clipHistory()
        fps = self.clip.fps
        if(frame_time < 1.0/fps):
            self.clip = self.clip.subclip(1/fps, self.clip.duration)
        elif(frame_time > self.clip.duration - 1.0/fps):
            self.clip = self.clip.subclip(self.clip.duration - 1.0/fps , self.clip.duration)
        else:
            first_clip = self.clip.subclip(0, frame_time - 0.5 * 1.0/fps)
            second_clip = self.clip.subclip(frame_time + 0.5 * 1.0/fps, self.clip.duration)
            self.clip = concatenate_videoclips([first_clip, second_clip])
        
        return self.clip

    def remove_frame_index(self, frame_index):
        self._clipHistory()
        fps = self.clip.fps
        frame_time = frame_index*1.0/fps
        first_clip = self.clip.subclip(0, frame_time - 0.5 * 1.0/fps)
        second_clip = self.clip.subclip(frame_time + 0.5 * 1.0/fps, self.clip.duration)
        self.clip = concatenate_videoclips([first_clip, second_clip])
        return self.clip

    def insert_frame(self, frame_path, frame_time):
        self._clipHistory()
        try:
            frame_clip = ImageClip(frame_path).set_duration(1.0/self.clip.fps)
            if frame_time < 1.0/self.clip.fps:
                self.clip =  concatenate_videoclips([frame_clip, self.clip])
            elif frame_time > self.clip.duration - 1.0/self.clip.fps:
                self.clip = concatenate_videoclips([self.clip.clip, frame_clip])
            else:
                first_clip = self.clip.subclip(0, frame_time - 0.5 * 1.0/self.clip.fps)
                second_clip = self.clip.subclip(frame_time + 0.5 * 1.0/self.clip.fps, self.clip.duration)
                self.clip =  concatenate_videoclips([first_clip, frame_clip, second_clip])
            
            return self.clip
        except:
            raise Exception('Could not find the frame for the given path: ' + frame_path)
            
            


    def save_clip(self, name_of_clip, path_optional = '', extension = ''):
        path = self.path_to_save if path_optional == '' else path_optional
        if extension == '':
            extension = '.mp4' if self.type == 'video' else '.mp3'
        try:
            self.clip.write_videofile(path + name_of_clip + extension)
        except:
            raise Exception('Could not save the clip in directory: ' + path + name_of_clip + extension)

    #Frames have to be ordered by number. Without numbers the order of the frames is random.
    #The frame name must include the ordering number: 'frame0.png' / '1frame.png' / 'frame1out.png' etc.
    #Currently only accepts images of type:
    #jpeg, jpg, png
    def make_video_from_frames(self, frames_path, frames_per_second):
        if not os.path.exists(frames_path):
            raise Exception('Directory does not exist')
        self._clipHistory()
        all_frames = []
        for frame in os.listdir(frames_path):
            framename = os.fsdecode(frame)
            extension = framename.split(".")[-1]
            if extension in ['jpeg', 'jpg','png'] :
                all_frames.append(frames_path + framename)
            else:
                continue
        #print(all_frames)
        # Assuming natural_keys function is defined
        all_frames.sort(key=self.natural_keys)
        clips = [ImageClip(m).set_duration(1.0/frames_per_second) for m in all_frames]
        concat_clip = concatenate_videoclips(clips)
        self.clip = concat_clip.set_fps(frames_per_second)
        return self.clip
    
    def mirror_at_x(self):
        self._clipHistory()
        self.clip = self.clip.fx(vfx.mirror_x)
        return self.clip

    def mirror_at_y(self):
        self._clipHistory()
        self.clip = self.clip.fx(vfx.mirror_y)
        return self.clip
    
    
    def change_speed(self, speed, start, end):
        self._clipHistory()
        if start < 0:
            start = 0
        if end < 0:
            end = 0
        if start > self.clip.duration:
            start = self.clip.duration
        if end > self.clip.duration:
            end = self.clip.duration

        before_speed = self.clip.subclip(0, start)
        after_speed = self.clip.subclip(end, self.clip.duration)
        speed_clip = self.clip.subclip(start, end)

        speed_clip.audio.write_audiofile("tempAudio.wav")

        # Assuming necessary imports for ffmpeg and other required libraries
        input_file = ffmpeg.input('tempAudio.wav')
        speed_up = ffmpeg.filter_(input_file, 'atempo', str(speed))
        out = ffmpeg.output(speed_up, 'tempAudio2.wav').overwrite_output().run()

        audio = AudioFileClip("tempAudio2.wav")

        speed_clip = speed_clip.speedx(speed)
        speed_clip = speed_clip.set_audio(audio)
        self.clip = concatenate_videoclips([before_speed, speed_clip, after_speed])
        return self.clip


def delete_frame_synchronous(clip, frame_time):
    fps = clip.fps
    if frame_time >= 0 and frame_time < clip.duration:
        frametime_norm = int(frame_time * fps) * 1/fps
        before = clip.get_frame(frametime_norm - 1/fps)
        after = clip.get_frame(frametime_norm + 1/fps)
        delete = clip.get_frame(frametime_norm)
        new_frame = np.add(after/2, before/2).astype(int)

        before_clip = clip.subclip(0, frametime_norm - 1/fps)
        after_clip = clip.subclip(frametime_norm + 1/fps, clip.duration)

        frame_clip = ImageClip(new_frame).set_duration(1.0/clip.fps)
        audio = clip.audio.copy()
        new_clip = concatenate_videoclips([before_clip, frame_clip, after_clip])
        new_clip.audio = audio
        return new_clip




def change_speed_segments(clip, intervals, speed_factor):
    clip.audio.write_audiofile("tempAudio.wav")
    stream = ffmpeg.input("tempAudio.wav")

    audio_segments = []
    prev_end = 0
    for interval in intervals:
        segment_start = interval[0]
        segment_end = interval[1]
        if prev_end < segment_start:
            audio_segments.append(stream.filter('atrim', start=prev_end, end=segment_start))
        audio_segments.append(
            stream.filter('atrim', start=segment_start, end=segment_end)
            .filter('atempo', speed_factor)
            .filter('asetpts', 'PTS-STARTPTS')
        )
        prev_end = segment_end
    if prev_end < float(ffmpeg.probe("tempAudio.wav")['format']['duration']):
        audio_segments.append(stream.filter('atrim', start=prev_end))
    stream = ffmpeg.concat(*audio_segments, v=0, a=1)
    stream = ffmpeg.output(stream, "tempAudio2.wav", acodec='pcm_s16le').overwrite_output()
    ffmpeg.run(stream, capture_stderr=True)

    audio = AudioFileClip("tempAudio2.wav")
    new_clip = clip.set_audio(audio)
    return new_clip


def save_audio_from_text_grid(clip, row, path_textgrid, path_to_save_audios, start, end):
    checkDirExists(path_to_save_audios)
    tg = textgrid.TextGrid.fromFile(path_textgrid)
    audio = clip.audio
    if end == 0:
        end = len(tg[row])
    for i in range(start, end, 1):
        minT = tg[row][i].minTime
        maxT = tg[row][i].maxTime
        audio_short = audio.subclip(minT - minT / 6000, maxT + maxT / 6000)
        name_of_short = str(i) + str(tg[row][i].mark) + ".wav"
        name_of_short = name_of_short.replace(":", "")
        audio_short.write_audiofile(path_to_save_audios + name_of_short, logger=None)


def create_audio_from_audios(name, path_to_audios, path_to_save):
    checkDirExists(path_to_save)
    all_shorts = []
    for short in os.listdir(path_to_audios):
        shortname = os.fsdecode(short)
        if shortname.endswith(".wav") or shortname.endswith(".mp3"):
            all_shorts.append(path_to_audios + shortname)
        else:
            continue

    all_shorts.sort(key=natural_keys)
    clips = [AudioFileClip(m) for m in all_shorts]
    concat_clip = concatenate_audioclips(clips)
    concat_clip.write_audiofile(path_to_save + name)
    


def get_text_grid_information(clip, text_of_interest, path_textgrid, path_save):
    checkDirExists(path_save)
    tg = textgrid.TextGrid.fromFile(path_textgrid)
    occasions = []
    for row in range(len(tg)):
        for column in range(len(tg[row])):
            if tg[row][column].mark == text_of_interest:
                occasions.append(str(tg[row][column].mark) + ": "
                                 + str(tg[row][column].minTime) + "s - " 
                                 + str(tg[row][column].maxTime)+ "s\n")

    filename = path_save + 'TextGridInfo-' + text_of_interest + '.txt'
    with open(filename, 'w') as f:
        for o in occasions:
            f.write(o)

def extract_text_occasions_from_grid(clip, text_of_interest, path_textgrid, path_save):
    checkDirExists(path_save)
    tg = textgrid.TextGrid.fromFile(path_textgrid)
    occasions = []
    for row in range(len(tg)):
        for column in range(len(tg[row])):
            if tg[row][column].mark == text_of_interest:
                occasions.append([tg[row][column].minTime, tg[row][column].maxTime])
    
    if isinstance(clip, VideoFileClip):
        audio = clip.audio
    else:
        audio = clip
    for o in range(len(occasions)):
        minT = occasions[o][0]
        maxT = occasions[o][1]
        audio_short = audio.subclip(minT-minT/6000,maxT+maxT/6000)
        name_of_short = str(o) + text_of_interest + '-' + str(minT)[:5] + ".wav"
        name_of_short = name_of_short.replace(":", "")
        audio_short.write_audiofile(path_save + name_of_short, logger=None)
























