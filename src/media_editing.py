# Part 1 - Media Editing
# 
# Authors: Christian Schuler & Dominik Hauser & Anran Wang
################################################################################

import ffmpeg
import os.path as path
from moviepy.editor import *
import re
import textgrid
import numpy as np
import imageio


"""
Editing class for video and audio files. It works mostly with video files at the moment.
Init:
    - path_to_file: Path to the file that should be edited
    - path_to_save: Standard path to save (most methods offer an optional parameter for their save-location)
"""
class editing():
    
    def __init__(self, path_to_file, path_to_save):
        self.path_to_file = path_to_file
        self.path_to_save = path_to_save
        if self._checkDirExists(path_to_file):
            self.clip, self.type = self._getClipFromPath(path_to_file)
            self.clip_history = []
        else:
            raise Exception('Input directory or file does not exist: ' + path_to_file)
     
        
    def _getClipFromPath(self, path_to_file):
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
            del self.clip_history[0]
    
    #Return the current (edited) clip
    def getClip(self):
        return self.clip
     
    #Return the audio of the current (edited) clip
    def getAudioClip(self):
        return self.clip.audio    
        
    #Sets the audio of the current edited clip
    def setAudioClip(self, path_to_clip):
        self._clipHistory()
        try:
            audio = AudioFileClip(path_to_clip)
            self.clip.set_audio(audio)
        except:
            raise Exception('Could not find the audio file or audio file has wrong format: ' + frame_path)


    """
    Functions for sorting by numbers. Remove anything than the numbers in a string.
    """
    def _atoi(self, text):
        return int(text) if text.isdigit() else text

    def _natural_keys(self, text):
        return [ self._atoi(c) for c in re.split(r'(\d+)', text)] 
    
    #Stores the last 5 clips and enables a basic undo-function
    def undo(self):
        if len(self.clip_history) >0:
            self.clip = self.clip_history[-1]
            del self.clip_history[-1]
        
    
    #Checks if dir exists
    def _checkDirExists(self, pathToCheck):
        return os.path.exists(pathToCheck)

    
    #Checks if dir exists, if not: creates dir
    def _checkDirExistsAndCreate(self, pathToCheck):
        if not os.path.exists(pathToCheck):
            os.makedirs(pathToCheck)
     
        
    #Cut the current clip 
    def cut(self, start, end):
        self._clipHistory()
        if start < end:
            if start < 0:
                start = 0
            if end < 0 or end > self.clip.duration:
                end = self.clip.duration
            
            self.clip.subclip(start, end)
    
    
    #Return a frame at a given time
    def getFrame(self, frame_time):
        if self.type == 'video':
            return self.clip.get_frame(frame_time)

    #Saves a frame at a given time. Requires the name for the frame.
    def saveFrame(self, frame_time, frame_name, extension = 'png'):
        if self.type == 'video':
            imageio.imwrite(self.path_to_save + frame_name  + '.' + extension, self.clip.get_frame(frame_time))


    #Saves all frames of the clip either in the standard save path or a given one
    def saveAllFrames(self, path_optional = '', extension = 'png'):
        if self.type == 'video':
            fps = self.clip.fps
            numberOfFrames = int(fps * self.clip.duration)
            path = self.path_to_save if path_optional =='' else path_optional
            self._checkDirExistsAndCreate(path)
            for f in range(numberOfFrames):
                frame = self.clip.get_frame(f*1.0/fps)
                normalized_array = (frame - np.min(frame)) / (np.max(frame) - np.min(frame))
                img = (normalized_array * 255).astype(np.uint8)
                imageio.imwrite(path + 'frame'+ str(f) + '.' + extension, img)
        
    
    #Removes a frame at a certain time
    def removeFrameTime(self, frame_time):
        if self.type == 'video':
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
            

    #Removes a frame at a given index
    def removeFrameIndex(self, frame_index):
        if self.type == 'video':
            self._clipHistory()
            fps = self.clip.fps
            frame_time = frame_index*1.0/fps
            first_clip = self.clip.subclip(0, frame_time - 0.5 * 1.0/fps)
            second_clip = self.clip.subclip(frame_time + 0.5 * 1.0/fps, self.clip.duration)
            self.clip = concatenate_videoclips([first_clip, second_clip])


    #Inserts a frame at a given index
    def insertFrame(self, frame_path, frame_time):
        if self.type == 'video':
            try:
                self._clipHistory()
                frame_clip = ImageClip(frame_path).set_duration(1.0/self.clip.fps)
                if frame_time < 1.0/self.clip.fps:
                    self.clip =  concatenate_videoclips([frame_clip, self.clip])
                elif frame_time > self.clip.duration - 1.0/self.clip.fps:
                    self.clip = concatenate_videoclips([self.clip.clip, frame_clip])
                else:
                    first_clip = self.clip.subclip(0, frame_time - 0.5 * 1.0/self.clip.fps)
                    second_clip = self.clip.subclip(frame_time + 0.5 * 1.0/self.clip.fps, self.clip.duration)
                    self.clip =  concatenate_videoclips([first_clip, frame_clip, second_clip])
                
            except:
                raise Exception('Could not find the frame for the given path: ' + frame_path)
            
            

    #Saves the clip to the standard save path or to the given optional path
    def saveClip(self, name_of_clip, path_optional = '', extension = ''):
        path = self.path_to_save if path_optional == '' else path_optional
        if extension == '':
            extension = '.mp4' if self.type == 'video' else '.mp3'
        try:
            self._checkDirExistsAndCreate(path)
            self.clip.write_videofile(path + name_of_clip + extension)
        except:
            raise Exception('Could not save the clip in directory: ' + path + name_of_clip + extension)


    #Frames have to be ordered by number. Without numbers the order of the frames is random.
    #The frame name must include the ordering number: 'frame0.png' / '1frame.png' / 'frame1out.png' etc.
    #Currently only accepts images of type:
    #jpeg, jpg, png
    def makeVideoFromFrames(self, frames_path, frames_per_second):
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
        all_frames.sort(key=self._natural_keys)
        clips = [ImageClip(m).set_duration(1.0/frames_per_second) for m in all_frames]
        concat_clip = concatenate_videoclips(clips)
        self.clip = concat_clip.set_fps(frames_per_second)
    
    #Mirrors the clip at the x-axis
    def mirrorAtX(self):
        if self.type == 'video':
            self._clipHistory()
            self.clip = self.clip.fx(vfx.mirror_x)

        
    #Mirrors the clip at the y-axis
    def mirrorAtY(self):
        if self.type == 'video':
            self._clipHistory()
            self.clip = self.clip.fx(vfx.mirror_y)

    
    #Changes the speed of the clip for a given segment
    def changeSpeed(self, speed, start, end):
        self._clipHistory()
        fps = self.clip.fps
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
        concat_clip = concatenate_videoclips([before_speed, speed_clip, after_speed])
        aud = concat_clip.audio.set_fps(44100)
        concat_clip = concat_clip.without_audio().set_audio(aud)
        concat_clip.set_fps(fps)
        self.clip = concat_clip


    #Delets a frame at a certain time and fuses the two neighboring frame to one to make the audio-video sync again
    def deleteFrameSynchronous(self, frame_time):
        if frame_time >= 0 and frame_time < self.clip.duration and self.type == 'video':
            self._clipHistory()
            fps = self.clip.fps
            frametime_norm = int(frame_time * fps) * 1/fps
            before = self.clip.get_frame(frametime_norm - 1/fps)
            after = self.clip.get_frame(frametime_norm + 1/fps)
            new_frame = np.add(after/2, before/2).astype(int)
    
            before_clip = self.clip.subclip(0, frametime_norm - 1/fps)
            after_clip = self.clip.subclip(frametime_norm + 1/fps, self.clip.duration)
    
            frame_clip = ImageClip(new_frame).set_duration(1.0/self.clip.fps)
            audio = self.clip.audio.copy()
            new_clip = concatenate_videoclips([before_clip, frame_clip, after_clip])
            new_clip.audio = audio
            self.clip = new_clip




    #Changes the speed for given segments of the video:
    #Segments are given like this: [[start_1, end_1], [start_2, end_2], ... ]
    def changeSpeedSegmentsAudio(self, intervals, speed_factor):
        self.clip.audio.write_audiofile("tempAudio.wav")
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
        self.clip = self.clip.set_audio(audio)



    #Saves certain audios/segments from the clip according to a given textgrid
    #Start/end index are in regards to how many elements from the textgrid should be saved
    def saveAudioFromTextGrid(self, row, path_textgrid, path_to_save_audios, start_index, end_index):
        self._checkDirExistsAndCreate(path_to_save_audios)
        tg = textgrid.TextGrid.fromFile(path_textgrid)
        audio = self.clip.audio
        if end_index < 0 or end_index > len(tg[row]):
            end_index = len(tg[row])
        for i in range(start_index, end_index, 1):
            minT = tg[row][i].minTime
            maxT = tg[row][i].maxTime
            audio_short = audio.subclip(minT - minT / 6000, maxT + maxT / 6000)
            name_of_short = str(i) + str(tg[row][i].mark) + ".wav"
            name_of_short = name_of_short.replace(":", "")
            audio_short.write_audiofile(path_to_save_audios + name_of_short, logger=None)

    #Creates an audio from many audios and saves it to a given path with a given name
    def createAudioFromAudios(self, name_of_file, path_to_audios, path_to_save = '', extension = ''):
        if self._checkDirExists(path_to_audios):
            self._checkDirExistsAndCreate(path_to_save)
            path = self.path_to_save if path_to_save == '' else path_to_save
            file_extension = '.mp3' if extension =='' else extension
            all_shorts = []
            for short in os.listdir(path_to_audios):
                shortname = os.fsdecode(short)
                if shortname.endswith(".wav") or shortname.endswith(".mp3"):
                    all_shorts.append(path_to_audios + shortname)
                else:
                    continue
        
            all_shorts.sort(key=self._natural_keys)
            clips = [AudioFileClip(m) for m in all_shorts]
            concat_clip = concatenate_audioclips(clips)
            concat_clip.write_audiofile(path + name_of_file + '.' + file_extension)
        else:
            raise Exception('Directory was not found: ' + path_to_audios)
    


    #Saves a txt file with information about a certain text_of_interest according to a given textGrid
    def getTextGridInformation(self, text_of_interest, path_textgrid, path_save):
        self._checkDirExistsAndCreate(path_save)
        try:
            tg = textgrid.TextGrid.fromFile(path_textgrid)
        except:
            raise Exception('Textgrid could not be found: ' + path_textgrid)
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

    #Saves occasions of text_of_interest (as audio) according to the given textGrid
    def extractTextOccasionsFromGrid(self, text_of_interest, path_textgrid, path_save, extension = ''):
        self._checkDirExistsAndCreate(path_save)
        
        try:
            tg = textgrid.TextGrid.fromFile(path_textgrid)
        except:
            raise Exception('Textgrid could not be found: ' + path_textgrid)
        occasions = []
        for row in range(len(tg)):
            for column in range(len(tg[row])):
                if tg[row][column].mark == text_of_interest:
                    occasions.append([tg[row][column].minTime, tg[row][column].maxTime])
        
        if self.type == 'video':
            file_extension = 'mp4' if extension == '' else extension
            video = self.clip
            for o in range(len(occasions)):
                minT = occasions[o][0]
                maxT = occasions[o][1]
                video_short = video.subclip(minT-minT/6000,maxT+maxT/6000)
                name_of_short = str(o) + text_of_interest + '-' + str(minT)[:5] + '.' + file_extension
                name_of_short = name_of_short.replace(":", "")
                video_short.write_videofile(path_save + name_of_short, logger=None)
        else:
            file_extension = 'mp3' if extension == '' else extension
            audio = self.clip
            for o in range(len(occasions)):
                minT = occasions[o][0]
                maxT = occasions[o][1]
                audio_short = audio.subclip(minT-minT/6000,maxT+maxT/6000)
                name_of_short = str(o) + text_of_interest + '-' + str(minT)[:5] + '.' + file_extension
                name_of_short = name_of_short.replace(":", "")
                audio_short.write_audiofile(path_save + name_of_short, logger=None)
























