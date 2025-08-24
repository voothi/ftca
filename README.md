# Flexible Text Copy Adapter (FTCA)
<img width="407" alt="{2793AAE1-85B1-4A0C-9D16-D1161511C907}" src="https://github.com/user-attachments/assets/7798a69e-956c-4fdd-9f79-72f56b82332a" />

## What is it?
This is a small utility that serves as an adapter, allowing to establish communication between a class of programs for assistance in reading in a foreign language and a local dictionary or translator, through the system clipboard.

In my case, it helps to easily connect local programs Lute (LWT) and GoldenDict for the ability to work locally, without an internet connection and automatically translate and view selected words from the Lute reading program in the GoldenDict-ng dictionary program.

- Selecting several words and automatically translating using the GoldenDict-ng option "Enable Scanning".
<img width="960" alt="{B42AB080-9EC6-4A3F-957C-98BB38748F5F}" src="https://github.com/user-attachments/assets/20c9bdfa-5f25-49b7-9eca-084304e94ba8" />

- Working with words. Copying the selected using Ctrl+C manually. The ability to select a separate morpheme of a word in the interface of the utility window.
<img width="960" alt="{72069897-3D0F-426E-82BC-4FB5A598F76D}" src="https://github.com/user-attachments/assets/8b884fbe-0db1-4e4c-b47d-bec144fcc17a" />

## Who is it for?
In general:
- Studying languages and mastering convenient tools for working with large texts.

In technical terms:
- Users of [Lute v3](https://github.com/LuteOrg/lute-v3) and similar programs for reading and translating selected portions of text, such as LWT, Readlang.org. Primarily aimed at use in local environments, without mandatory internet connectivity.
- Users of GoldenDict.

## What problem does this program solve?
A utility for solving the problem of translating individual words in [Lute v3](https://github.com/LuteOrg/lute-v3).

[Issue #593 — Revision of the logic of copying a word and substring of text from the main panel](https://github.com/LuteOrg/lute-v3/issues/593)

## How does it work?
https://github.com/user-attachments/assets/4ae740ae-c729-4405-b80a-7b225c7641b1

## How to get started?
- Download. You can perform a clone or visit the Releases page. The project consists of three main files: `ftca.py` (the server), `index.html` (the web page), and `launcher.py` (a helper script for multi-line support in GoldenDict).

- Check that the Python interpreter is installed on your system.

- Run.
You can run the `ftca-start.cmd` script if you have Windows.  
You can also simply run the command `python ftca.py` directly from the terminal.
The web server will start.  
Do not close the terminal window until you have finished working with the utility. Closing the window will terminate the web server.

- **Go to the address in your browser to test the functionality.**
See the "URL Parameters" and "How to check functionality?" sections below for examples.

- Provide permission for the page to use the clipboard.

## URL Parameters
The utility's behavior is controlled by parameters in the URL:

- **`s`**: The text content to display in the text area. The text should be standard URL-encoded.
  - *Example:* `s=Hello%20World`

- **`s_b64`**: The text content, encoded in Base64. This is the required method for reliably passing multi-line text from external programs.
  - *Example:* `s_b64=SGVsbG8KV29ybGQ=` (for "Hello\nWorld")

- **`clipboard=true`**: If this parameter is present, the script will automatically attempt to copy the content of the text area to the system clipboard upon loading.

- **`multiline=true`**: This flag must be used in conjunction with `s_b64` to ensure the server decodes and displays the Base64 content.

- **`rows`**: An integer that sets the initial height (number of visible lines) of the text area.
  - *Example:* `rows=15`
  - *Default:* If not specified, the height defaults to `4` lines.

## How to use in GoldenDict (Single-line text)?
This utility can be used not only with Lute but also within GoldenDict as a "Program" dictionary. This allows you to send the current search term to a new browser tab for easier editing or further processing.

This is ideal for single words or short phrases without line breaks.

<img width="960" alt="{F8846A14-2782-4FBE-A3EC-040F8E5EEF45}" src="https://github.com/user-attachments/assets/bebdc522-bb85-4cf3-8bf4-1794eb7b64f7" />

#### Setup:
Go to `GoldenDict-ng Main Window — Dictionaries — Sources — Programs` and add a new entry. You can optionally add the `&rows=...` parameter to control the initial size of the text area.

```
[x] Enabled
Type: Audio (or Html)
Name: FTCA
Command Line: "C:\Program Files\Google\Chrome\Application\chrome.exe" http://127.0.0.1:5010/?clipboard=true&rows=8&s="%GDWORD%"
```
<img width="960" alt="{56ED9E95-983C-4660-A92A-3EA1E0E91033}" src="https://github.com/user-attachments/assets/25328302-f275-4130-892a-0f8b657489fb" />

## How to use with multi-line text in GoldenDict?
When passing long text with line breaks from GoldenDict, the standard command-line method will fail and merge everything into a single line.

To preserve line breaks, we must use the included `launcher.py` helper script. It safely encodes the text using Base64 before launching the browser. Additionally, it automatically sets the text area height to **20 rows** (`rows=20`) for better viewing of multi-line content.

#### Setup:
Go to `GoldenDict-ng Main Window — Dictionaries — Sources — Programs` and use the following command line structure:

```
cmd /c "C:\path\to\your\python.exe" "C:\path\to\your\ftca\folder\launcher.py" "%GDWORD%"
```

You **must** replace the placeholder paths with the actual full paths on your system.

- **`"C:\path\to\your\python.exe"`**: The full path to your Python interpreter.
  *(Example: `"C:\Users\YourUser\AppData\Local\Programs\Python\Python312\python.exe"`)*
- **`"C:\path\to\your\ftca\folder\launcher.py"`**: The full path to the `launcher.py` script.
  *(Example: `"D:\MyTools\ftca\launcher.py"`)*

**Example of a complete command:**
```
cmd /c "C:\Users\User\AppData\Local\Programs\Python\Python312\python.exe" "D:\MyTools\ftca\launcher.py" "%GDWORD%"
```
<img width="960" alt="{2A58A109-50DB-47F8-AB31-EC481A71A823}" src="https://github.com/user-attachments/assets/cf4e736a-25b5-4e6a-9805-798a4379cd50" />

## What are the advantages?
- **Versatility**. Can be integrated into [Lute](https://github.com/LuteOrg/lute-v3) and similar programs where interaction with dictionaries is done through HTTP requests.
- **Offline operation**. Allows for an offline workflow between reading software and a local dictionary like GoldenDict-ng.
- **Multi-line text preservation**. Reliably handles text with line breaks from applications like GoldenDict, which is not possible with direct command-line calls.
- **Minimalism**. Minimal software dependencies.
- **Cross-platform compatibility**. Works wherever a Python interpreter and a browser can run.
- **Easy integration**. Can be easily included in an existing set of tools.

## What inspired it?
I accidentally discovered that when making a request like `https://m.dict.cc/deutsch-russisch/test.html`, the input field on the page loads with the search term already selected (as if by Ctrl+A). This JavaScript-powered feature allows for immediate copying to the clipboard, which inspired the core functionality of FTCA.

## How to use Dark Mode or Dark Theme?
If you use a browser extension like [Dark Reader](https://github.com/darkreader/darkreader), you can enable it for the FTCA page. Simply open a link like `http://127.0.0.1:5010/?s=test` and activate the plugin for this site.

<img width="960" alt="image" src="https://github.com/user-attachments/assets/c4aabcf3-aead-41b9-bfa4-5582591a4a48" />

## What are the technical features?
The utility runs a lightweight, dependency-free HTTP server using Python's standard library. It serves a single HTML/JS page that acts as the adapter. For multi-line text, a helper script uses Base64 encoding to ensure data integrity during transmission via the command line.

## What are the system environment prerequisites?
- Python 3.x.
- Chrome or a browser that supports the Modern Clipboard API.

## In what environment was it tested?
- Windows 11.
- Python 3.12.7.
- Chrome Version 122.0.6261.95 (Official Build) (64-bit).
- LUTE: Learning Using Texts v3, Version: 3.10.1.
- GoldenDict-ng 24.04.12-alpha.20240412.000451.

## How to configure in the Lute v3 web interface?
Settings — Languages — [Your Language] — Edit  
Dictionaries — Add dictionary  
- **Type**: Terms
- **Open in**: Pop-up window
- **URI**: `http://127.0.0.1:5010/?clipboard=true&rows=8&s=[LUTE]`
- **Is active?**: `true`

*(Note: You can adjust the `rows=8` value to your preferred initial height.)*

## How to allow Clipboard Read Access (Chrome)?
The script uses the Modern Clipboard API, which requires you to grant the page permission to interact with the clipboard.

<img width="407" alt="{2793AAE1-85B1-4A0C-9D16-D1161511C907}" src="https://github.com/user-attachments/assets/8b0186e3-1476-46c3-afa5-f80ebb59581a" />

## How to check functionality?
Run the `ftca.py` server.

Open one of the links below in your browser.  

- **Option 1 (Simple text, default size)**
http://127.0.0.1:5010/?s=test%20test

- **Option 2 (With clipboard copy)**
http://127.0.0.1:5010/?clipboard=true&s=test

- **Option 3 (With custom height)**
http://127.0.0.1:5010/?s=This%20is%20a%20test%20in%20a%20taller%20box&rows=10

The page should load with your text in the input field, fully selected. If `clipboard=true` is used and permission is granted, the text will also be automatically copied to your clipboard. For multi-line tests, use the GoldenDict setup described above.

## What about the security of my buffer data?
This utility does not transmit your data to the internet. It operates locally on your PC, transmitting data between applications via the loopback network interface (`127.0.0.1`). While it doesn't store data on disk, it is processed in RAM. Assess your own risks when working with sensitive information. It is strongly recommended not to expose this server to any address other than the loopback address.

## Why doesn't it work?
- Ensure no other application is using port `5010`.
- Make sure you have only one instance of the `ftca.py` script running. Check your system's process manager for `python` processes related to `ftca`.
- If using the multi-line method, double-check that the paths to `python.exe` and `launcher.py` in your GoldenDict command are correct and enclosed in double quotes.

## License
MIT License.

## Author's Disclaimer
The software is provided "as is" without any warranties. The author is not responsible for any damages or issues arising from the use of this software. Users are advised to use it at their own risk.

## Stars
If you find this utility helpful, please consider starring the repository to support the developer's efforts.
