from google.colab import drive
drive.mount('/content/gdrive')
!ls /content/gdrive/My Drive
model_save_name = 'classifier.pt'
path = F"/content/gdrive/My Drive/{model_save_name}" 
torch.save(model.state_dict(), path)