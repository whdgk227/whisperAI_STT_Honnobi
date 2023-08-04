
def getWhisperModel(modelType = "large"):
  # model parameter - tiny, base, small, medium, large
  print("\nWhisperAI-"+modelType+" 모델을 불러옵니다. 안전하게 완료 될 때 까지 잠시 기다려주세요.\n")
  model = whisper.load_model(modelType,device = "cuda") # // device - cuda = GPU version
  # model = whisper.load_model("large") # CPU version
  print("\nWhisperAI-"+modelType+" 모델 불러오기를 성공했습니다.\n다음 단계를 진행 해주세요.\n")

  return model

