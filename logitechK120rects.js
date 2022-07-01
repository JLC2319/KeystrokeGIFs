const keys = [
    { key: 'esc', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f1', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f2', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f3', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f4', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f5', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f6', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f7', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f8', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f9', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f10', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f11', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f12', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'print screen', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'scroll lock', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix 
    { key: 'pause|break', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix 
    { key: '`', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '1', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '2', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '3', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '4', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '5', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '6', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '7', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '8', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '9', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '0', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '-', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '=', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'backspace', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix   
    { key: 'tab', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'q', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'w', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'e', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'r', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 't', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'y', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'u', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'i', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'o', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'p', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '[', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: ']', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '\\', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'caps lock', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'a', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 's', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'd', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'f', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'g', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'h', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'j', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'k', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'l', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: ';', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: "'", rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'enter', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'shift', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'z', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'x', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'c', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'v', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'b', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'n', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'm', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: ',', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '.', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: '/', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'shift', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'ctrl', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'window', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'alt', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'space', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'alt', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'window', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'doc', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'ctrl', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'insert', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'home', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'page up', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'delete', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'end', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'page down', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'up', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'left', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'down', rect: { x: 0, y: 0, w: 0, h: 0 } }, //Fix
    { key: 'right', rect: { x: 0, y: 0, w: 0, h: 0 } } //Fix
  ]


