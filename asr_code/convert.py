from pydub import AudioSegment

# 把这里的 "jianying.wav" 换成实际的文件名
input_file = "jianying.wav" 
output_file = "audio_sample.wav"

print("正在读取并转换音频...")
try:
    audio = AudioSegment.from_file(input_file)
    
    # 核心转换：变单声道，变 16kHz
    audio = audio.set_channels(1)
    audio = audio.set_frame_rate(16000)
    
    # 导出给 Vosk 用的标准文件
    audio.export(output_file, format="wav")
    print(f"转换成功！快去用 main.py 跑一下 {output_file} 吧！")
except Exception as e:
    print(f"转换失败: {e}")
    print("提示：如果报错说找不到 ffmpeg，请告诉我！")