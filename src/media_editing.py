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

    
    
    
    
    

"""
Functions for sorting by numbers. Remove anything than the numbers in a string.
"""
def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]        
    
    
#Returns the audio of the clip
def getAudioClip(clip):
    return clip.audio

#Sets the audio of the current clip
def setAudioClip(clip,audio_clip):
    return clip.set_audio(audio_clip)
    
        

#Creates DIR when not existent
def checkDirExists(pathToCheck):
    if not os.path.exists(pathToCheck):
        os.makedirs(pathToCheck)

def cut(clip, start, end):
    if start < 0:
        start = 0
    if end == -1 or end > clip.duration:
        end = clip.duration

    return clip.subclip(start, end)

def get_frame(clip, frame_time):
    return clip.get_frame(frame_time)

def save_frame(clip, frame_time, path_to_save):
    imageio.imwrite(path_to_save + 'FRAME' +str(frame_time) +  '.png', get_frame(clip, frame_time))


#Saves all frames of a video as individual image files.
def save_all_frames(clip, path_to_save):
    fps = clip.fps
    numberOfFrames = int(fps * clip.duration)
    checkDirExists(path_to_save)
    for f in range(numberOfFrames):
        frame = clip.get_frame(f*1.0/fps)
        normalized_array = (frame - np.min(frame)) / (np.max(frame) - np.min(frame))
        img = (normalized_array * 255).astype(np.uint8)
        imageio.imwrite(path_to_save + 'frame'+ str(f) + '.png', img)
        #fromarray(frame).save(path_to_save + 'frame'+ str(f) + '.png')


#Removes a frame at a specific time from the video.
def remove_frame_time(clip, frame_time):
    fps = clip.fps
    if(frame_time < 1.0/fps):
        return clip.subclip(1/fps, clip.duration)
    elif(frame_time > clip.duration - 1.0/fps):
        return clip.subclip(clip.duration - 1.0/fps , clip.duration)
    else:
        first_clip = clip.subclip(0, frame_time - 0.5 * 1.0/fps)
        second_clip = clip.subclip(frame_time + 0.5 * 1.0/fps, clip.duration)
        return concatenate_videoclips([first_clip, second_clip])

#Removes a frame at a specific index from the video.
def remove_frame_index(clip, frame_index):
    fps = clip.fps
    frame_time = frame_index*1.0/fps
    first_clip = clip.subclip(0, frame_time - 0.5 * 1.0/fps)
    second_clip = clip.subclip(frame_time + 0.5 * 1.0/fps, clip.duration)
    return concatenate_videoclips([first_clip, second_clip])


#Inserts an image frame at a specific time in the video.
def insert_frame(clip, frame_location, frame_time):
    frame_clip = ImageClip(frame_location).set_duration(1.0/clip.fps)
    if frame_time < 1.0/clip.fps:
        return concatenate_videoclips([frame_clip, clip])
    elif frame_time > clip.duration - 1.0/clip.fps:
        return concatenate_videoclips([clip, frame_clip])
    else:
        first_clip = clip.subclip(0, frame_time - 0.5 * 1.0/clip.fps)
        second_clip = clip.subclip(frame_time + 0.5 * 1.0/clip.fps, clip.duration)
        return concatenate_videoclips([first_clip, frame_clip, second_clip])



def save_clip(clip, nameOfClip, path_to_save):
    clip.write_videofile(path_to_save + nameOfClip)



#Creates a video from a directory of image frames.
def make_video_from_frames(frames_location, frames_per_second):
    if not os.path.exists(frames_location):
        raise Exception('Directory does not exist')

    all_frames = []
    for frame in os.listdir(frames_location):
        framename = os.fsdecode(frame)
        if framename.endswith(".png") or framename.endswith(".jpg"): 
            all_frames.append(frames_location + framename)
        else:
            continue

    # Assuming natural_keys function is defined
    all_frames.sort(key=natural_keys)
    clips = [ImageClip(m).set_duration(1.0/frames_per_second) for m in all_frames]
    concat_clip = concatenate_videoclips(clips)
    return concat_clip.set_fps(frames_per_second)



#Removes a frame at a specific time and makes the video synchronous again
# by fusing the two adjecent frames to one
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


#Flips the video horizontally.
def mirror_at_x(clip):
    return clip.fx(vfx.mirror_x)


#Flips the video vertically.
def mirror_at_y(clip):
    return clip.fx(vfx.mirror_y)



#Changes the speed of the video and audio.
def change_speed(clip, speed, start, end):
    if start < 0:
        start = 0
    if end < 0:
        end = 0
    if start > clip.duration:
        start = clip.duration
    if end > clip.duration:
        end = clip.duration

    before_speed = clip.subclip(0, start)
    after_speed = clip.subclip(end, clip.duration)
    speed_clip = clip.subclip(start, end)

    speed_clip.audio.write_audiofile("tempAudio.wav")

    # Assuming necessary imports for ffmpeg and other required libraries
    input_file = ffmpeg.input('tempAudio.wav')
    speed_up = ffmpeg.filter_(input_file, 'atempo', str(speed))
    out = ffmpeg.output(speed_up, 'tempAudio2.wav').overwrite_output().run()

    audio = AudioFileClip("tempAudio2.wav")

    speed_clip = speed_clip.speedx(speed)
    speed_clip = speed_clip.set_audio(audio)
    return concatenate_videoclips([before_speed, speed_clip, after_speed])



#Changes the speed of specified segments in the video.
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



#Saves short audio snippets according to the timings from a TextGrid file.
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



#Combines multiple audio files into a single audio file.
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
    


#Extracts timings of a specific text from a TextGrid file and writes it to a text file.
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


#Extracts audio snippets for a specific text from a TextGrid file and saves them as individual audio files.
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



#Removes every occasion of a given text according to timings in the textgrid file. 
# The functions tries to sync the video again by inserting fusion frames.
def remove_text_occurrences(clip, text_of_interest, path_to_textgrid):
    tg = textgrid.TextGrid.fromFile(path_to_textgrid)
    intervals_to_remove = []
    if  isinstance(text_of_interest,list):
        # Find occurrences of the text in the TextGrid
        for row in range(len(tg)):
            for column in range(len(tg[row])):
                if tg[row][column].mark in text_of_interest:
                    intervals_to_remove.append([tg[row][column].minTime, tg[row][column].maxTime])
                    
    else:    
        # Find occurrences of the text in the TextGrid
        for row in range(len(tg)):
            for column in range(len(tg[row])):
                if tg[row][column].mark == text_of_interest:
                    intervals_to_remove.append([tg[row][column].minTime, tg[row][column].maxTime])

    # Load the video and audio files
    video = clip
    audio = clip.audio

    # Remove audio occurrences
    audio_segments = []
    prev_end = 0
    for interval in intervals_to_remove:
        prev_end_est = prev_end-prev_end/6000 if prev_end != 0 else 0
        audio_segments.append(audio.subclip(prev_end_est, interval[0]+interval[0]/6000))
        prev_end = interval[1]

    audio_segments.append(audio.subclip(prev_end, audio.duration))
    new_audio = concatenate_audioclips(audio_segments)
    print(len(audio_segments))
    
    # Remove video occurrences
    video_segments = []
    prev_end = 0
    for interval in intervals_to_remove:
        video_segments.append(video.subclip(prev_end, interval[0]))

        # Merge video frames around the occurrence
        prev_frame = video.get_frame(interval[0] - 1 / video.fps)
        next_frame = video.get_frame(interval[1])
        merged_frame = (prev_frame * 0.5 + next_frame * 0.5).clip(0, 255).astype('uint8')
        video_segments.append(ImageClip(merged_frame, duration=1 / video.fps))

        prev_end = interval[1]

    video_segments.append(video.subclip(prev_end, video.duration))
    new_video = concatenate_videoclips(video_segments)

    # Replace the audio of the new video
    final_video = new_video.set_audio(new_audio)

    return final_video

    
    
#Changes the speed of text occurances in the video.
# The functions tries to sync the video again by inserting fusion frames.
def speed_text_occurrences(clip, text_of_interest, path_to_textgrid, speed):
    tg = textgrid.TextGrid.fromFile(path_to_textgrid)
    intervals_to_speed = []
    
    if  isinstance(text_of_interest,list):
    # Find occurrences of the text in the TextGrid
        for row in range(len(tg)):
            for column in range(len(tg[row])):
                if tg[row][column].mark in text_of_interest:
                    intervals_to_speed.append([tg[row][column].minTime, tg[row][column].maxTime])
    else:
        for row in range(len(tg)):
            for column in range(len(tg[row])):
                if tg[row][column].mark == text_of_interest:
                    intervals_to_speed.append([tg[row][column].minTime, tg[row][column].maxTime])
    

    # Load the video and audio files
    video = clip
    audio = clip.audio
    
    clip = change_speed_segments(clip, intervals_to_speed, speed)

    return clip





def main():
    parser = argparse.ArgumentParser(description='Input for editing script')
    parser.add_argument('-path', type=str)
    parser.add_argument('-name', type=str)
    parser.add_argument('-cut', nargs=3)
    parser.add_argument('-speedChange', nargs=3)
    parser.add_argument('-saveAudioFromGrid', nargs='+')
    parser.add_argument('-makeAudioFromAudios', nargs = 3)
    parser.add_argument('-saveAllFrames', nargs=1)
    parser.add_argument('-extractTextGridOccasions', nargs = 3)
    parser.add_argument('-deleteFrameSync', nargs = 1)
    parser.add_argument('-saveFrame', nargs = 2)
    parser.add_argument('-removeFrame', nargs = 2)
    parser.add_argument('-insertFrame', nargs = 3)
    parser.add_argument('-makeVideoFromFrames', nargs = 3)
    parser.add_argument('-mirrorX', nargs = 1)
    parser.add_argument('-mirrorY', nargs = 1)
    parser.add_argument('-speedChangeSegments', nargs = 3)
    parser.add_argument('-textGridInformation', nargs = 3)
    parser.add_argument('-setAudio', nargs = 2)
    parser.add_argument('-removeOccurances', nargs = 3)
    args = parser.parse_args()
    
    
    path_to_file = args.path
    
    if path_to_file == None:
        path_to_file = "./"

    def getVideoClipFromParser():
        comletePath = path_to_file+args.name
        return VideoFileClip(comletePath)
        
    def getAudioClipFromParser():
        comletePath = path_to_file+args.name
        return AudioFileClip(comletePath)
    
    def getClipFromParser():
        try:
            return getVideoClipFromParser()
        except:
            pass
        
        try:
            return getAudioClipFromParser()
        except:
            raise Exception('File is neither a video nor an audio file.')
        
        
    if args.removeOccurances !=None:
        clip = getVideoClipFromParser()
        text_of_interest = args.removeOccurances[0]
        path_textgrid = args.removeOccurances[1]
        path_to_save = args.removeOccurances[2]
        clip = remove_text_occurrences(clip, text_of_interest, path_textgrid)
        save_clip(clip, 'OCC_RM_' + args.name, path_to_save)
    
    if args.setAudio != None:
        videoClip = getVideoClipFromParser()
        audioClip = AudioFileClip(path_to_file+args.setAudio[0])
        path_to_save = args.setAudio[1]
        clip = setAudioClip(videoClip, audioClip)
        save_clip(clip,'NEW_AUDIO' + args.name, path_to_save)
        
    if args.speedChangeSegments != None:
        clip = getVideoClipFromParser()
        path_to_intervals_file = args.speedChangeSegments[0]
        speed_factor = float(args.speedChangeSegments[1])
        path_to_save = args.speedChangeSegments[2]
        
        with open(path_to_intervals_file, 'r') as f:
            intervals_of_speed_change = [list(map(float, line.strip().split(','))) for line in f.readlines()]
        
        clip = change_speed_segments(clip, intervals_of_speed_change, speed_factor)
        save_clip(clip, 'SPEED_SEGMENTS' + args.name, path_to_save)    
        
    if args.mirrorX != None:
        clip = getVideoClipFromParser()
        clip = mirror_at_x(clip)
        path_to_save = args.mirrorX[0]
        save_clip(clip, 'MIRROR_X' + args.name, path_to_save)

    if args.mirrorY != None:
        clip = getVideoClipFromParser()
        clip = mirror_at_y(clip)
        path_to_save = args.mirrorY[0]
        save_clip(clip, 'MIRROR_Y' + args.name, path_to_save)    
        
    if args.textGridInformation != None:
        clip = getClipFromParser()
        text_of_interest = args.textGridInformation[0]
        path_to_textgrid = args.textGridInformation[1]
        path_save = args.textGridInformation[2]
        get_text_grid_information(clip, text_of_interest, path_to_textgrid, path_save)
        
        
    if args.insertFrame != None:
        clip = getVideoClipFromParser()
        frame_time = float(args.insertFrame[0])
        frame_location = args.insertFrame[1]
        path_to_save = args.insertFrame[2]
        clip = insert_frame(clip, frame_location, frame_time)
        save_clip(clip, 'FRAME_INSERT' + args.name, path_to_save)

    if args.makeVideoFromFrames != None:
        frame_location = args.makeVideoFromFrames[0]
        frames_per_second = float(args.makeVideoFromFrames[1])
        path_to_save = args.makeVideoFromFrames[2]
        clip = make_video_from_frames(frame_location, frames_per_second)
        save_clip(clip, 'VIDEO_FROM_FRAMES' + args.name, path_to_save) 
    
    
    if args.removeFrame != None:
        clip = getVideoClipFromParser()
        frame_time = float(args.removeFrame[0])
        path_to_save = args.removeFrame[1]
        clip = remove_frame_time(clip, frame_time)
        save_clip(clip, 'FRAME_REMOVE' + args.name, path_to_save)
    
    if args.saveFrame != None:
        clip = getVideoClipFromParser()
        frame_time = args.saveFrame[0]
        path_to_save = args.saveFrame[1]
        save_frame(clip, frame_time, path_to_save)
    
    
    if args.saveAllFrames != None:
        clip = getVideoClipFromParser()
        location = args.save_all_frames[0]
        save_all_frames(clip, location)
        
        
    if args.cut != None:
        clip = getVideoClipFromParser()
        startEnd = args.cut
        start = float(startEnd[0])
        end = float(startEnd[1])
        path_to_save = args.cut[2]
        clip = cut(clip, start, end)
        save_clip(clip, "CUT" + args.name, path_to_save)
    
    
    
    if args.speedChange != None:
        clip = getVideoClipFromParser()
        startEndSpeed = args.speedChange
        start = float(startEndSpeed[0])
        end = float(startEndSpeed[1])
        speed = float(startEndSpeed[2])
        path_to_save = args.speedChange[3]
        clip = change_speed(clip, speed, start, end)
        save_clip(clip, "SPEED" + args.name, path_to_save)
        

    if args.deleteFrameSync != None:
        clip = getVideoClipFromParser()
        frame_time = float(args.deleteFrameSync[0])
        clip = delete_frame_synchronous(clip,frame_time)
        save_clip(clip, 'frameDeleteSync' + args.name, path_to_file)
    

    if args.extractTextGridOccasions != None:
        clip = getClipFromParser()
        text = args.extractTextGridOccasions[0]
        tg_path = args.extractTextGridOccasions[1]
        save_path = args.extractTextGridOccasions[2]
        extract_text_occasions_from_grid(clip, text, tg_path, save_path)
            
        
    if args.makeAudioFromAudios != None:
        name_of_audio = args.makeAudioFromAudios[0]
        path_audios = args.makeAudioFromAudios[1]
        path_save = args.makeAudioFromAudios[2]
        create_audio_from_audios(name_of_audio,path_audios,path_save)
    

    if args.saveAudioFromGrid != None:
        clip = getClipFromParser()
        params = args.saveAudioFromGrid
        row = int(params[0])
        path_grid = params[1]
        path_save_audio = params[2]
        start = 0
        end = 0
        if len(params) > 3:
            start = params[3]
            start = int(start) if type(start) is str and start.isdigit() else 0
        if len(params)>4:
            end = params[4]
            end = int(end) if type(end) is str and end.isdigit() else 0
        save_audio_from_text_grid(clip, row,path_grid, path_save_audio, start, end)
        
    
  
    
    
    
if __name__ == "__main__":
    main()






















































