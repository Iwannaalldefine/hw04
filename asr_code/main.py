import wave
import sys
import json
from vosk import Model, KaldiRecognizer

# 1. 加载 Vosk 模型 (指向你刚刚重命名的 model 文件夹)
model_path = "model" 
try:
    model = Model(model_path)
except Exception as e:
    print(f"模型加载失败，请检查 '{model_path}' 目录是否存在。错误: {e}")
    sys.exit(1)

# 2. 读取音频文件 (注意：Vosk 要求 16kHz, 单声道, 16-bit 的 WAV 文件)
# 剪映导出的音频转换好并命名为 audio_sample.wav
audio_file = "audio_sample.wav" 
try:
    wf = wave.open(audio_file, "rb")
except FileNotFoundError:
    print(f"找不到音频文件：{audio_file}。请先完成任务二并准备好音频。")
    sys.exit(1)

# 校验音频格式
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print("音频格式不符合要求：必须是单声道 (mono) PCM WAV 文件。")
    sys.exit(1)

# 3. 初始化识别器
rec = KaldiRecognizer(model, wf.getframerate())
rec.SetWords(True)

# 4. 开始流式识别 (模拟分块读取)
print("开始本地离线识别...")
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        # 如果需要查看实时流式识别的过程，可以取消下面这行的注释
        # print(json.loads(rec.Result())) 
        pass

# 5. 输出最终文本
result = json.loads(rec.FinalResult())
recognized_text = result.get("text", "").replace(" ", "") # 中文识别结果通常带有空格，清理一下
print("\n--- 最终识别结果 ---")
print(recognized_text)