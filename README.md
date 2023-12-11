# Add To Search Menu
A simple program that adds a given program to the windows search index. It does this by adding
a shortcut of the program to the start menu folder and then updating the search index. Usually the
path: `C:\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs`

## Usage
```bash
a2sm.exe <path to program> <name of shortcut>
```

## Example
```bash
a2sm.exe "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" "Google Chrome"
```

## Notes
- Consider adding the exe to your path so you can run it from anywhere
- I'm on that good kush and alcohol 😎
