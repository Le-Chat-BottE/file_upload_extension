import gradio as gr

def on_ui_tabs():
  with gr.Blocks() as upload:
    with gr.Tab('Upload'):
      gr.File(···)
  return (upload, 'Upload', 'upload'),

script_callbacks.on_ui_tabs(on_ui_tabs)
