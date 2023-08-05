#!/usr/bin/env python3
import time
import PySimpleGUI as psg

def formatLapAndRun(lap: int, run: int) -> str:
    fmtIval = lambda i: f'{int(i/60):02d}:{int(i%60):02d}'
    return f'{fmtIval(lap)}\n{fmtIval(run)}'

defaultFontSize = 20
fontSize = defaultFontSize

layout = [[psg.Text(text='00:00\n00:00', 
                    key='-LAP-',
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    justification='center',
                    font=f'sans {fontSize}')]]

window = psg.Window(title='stopwatch',
                    layout=layout,
                    resizable=True,
                    finalize=True)

startSize = window.size
lastSize = startSize

runStart = int(time.time())
lapStart = runStart

while True:
    event, _ = window.read(timeout=250) # 4+ fps

    if event == psg.WIN_CLOSED:
        break
    elif event == '-LAP-':
        lapStart=int(time.time())

    if window.size != lastSize: # rescale
        lastSize = window.size
        newScale = min(lastSize[0]/startSize[0], lastSize[1]/startSize[1])
        fontSize = int(defaultFontSize*newScale)

    now = int(time.time())
    lapTime = int(now-lapStart)
    runTime = int(now-runStart)

    window['-LAP-'].update(value=formatLapAndRun(lapTime, runTime),
                           font=f'sans {fontSize}')

window.close()
