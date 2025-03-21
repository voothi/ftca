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

## How else can you use in GoldenDict and others?
Another use case for the utility has opened. The utility can be used not only with Lute, but also in the GoldenDict dictionary program as a dictionary similar to how it is configured in Lute.
This solution allows you to open a page with text in the dictionary window by clicking on a link in the dictionary window. This can be convenient for editing a query on the fly and for analyzing complex lexical constructions. It can be used as an additional intermediate buffer for working with text, which is not possible with the GoldenDict dictionary itself. It only has single-line input, which is not convenient when using in translation mode or in translation mode under the cursor.

Using the window in the browser and the side window of the GoldenDict dictionary.
<img width="960" alt="{F8846A14-2782-4FBE-A3EC-040F8E5EEF45}" src="https://github.com/user-attachments/assets/bebdc522-bb85-4cf3-8bf4-1794eb7b64f7" />

Setting up the utility in the GoldenDict dictionary.
GoldenDict-ng  
Main Window — Dictionaries — Sources — Programs
```
[x]
FTCA
Audio
"C:\Program Files\Google\Chrome\Application\chrome.exe" http://127.0.0.1:5010/?clipboard=true&s="%GDWORD%"
```
<img width="960" alt="{56ED9E95-983C-4660-A92A-3EA1E0E91033}" src="https://github.com/user-attachments/assets/25328302-f275-4130-892a-0f8b657489fb" />
<img width="960" alt="{2A58A109-50DB-47F8-AB31-EC481A71A823}" src="https://github.com/user-attachments/assets/cf4e736a-25b5-4e6a-9805-798a4379cd50" />


## How to get started?
- Download. You can perform a clone or visit the Releases page.

- Check that the Python interpreter is installed on your system.

- Run.
You can run the `ftca-start.cmd` script if you have Windows.  
You can also simply run the command directly from the terminal from the `ftca-start.cmd` file.
The web server will start.  
Do not close the black terminal window until you have finished working with the utility. Closing the window will end the work of the web server, which publishes the page and it will stop responding.

- Go to the address in your browser
http://127.0.0.1:5010/?clipboard=true&s=test
Next, you can test as described in a separate item below, on this page, in the testing section.  

- Provide permission for the page to use the clipboard.
See below for a separate item on setting up ("How to configure in the Lute v3 web interface").

## What are the advantages?
- Versatility. Can be integrated into [Lute](https://github.com/LuteOrg/lute-v3) and similar programs where interaction with dictionaries is done through HTTP requests with a predefined template URL. Anywhere that supports translator configuration by URL. Google, DeepL, Yandex, PONS, etc.
- Offline operation. Allows, as an adapter between reading software and a local program for translating and viewing words, to establish offline functionality. It does not require an Internet connection, unlike external HTTP dictionaries and translators. The recommended translation program is GoldenDict-ng.
- Minimalism. Minimal software dependencies.
- Cross-platform compatibility. Works wherever a Python interpreter and a browser can run.
- Easy integration. Can be easily included in an existing set of tools without the need for modifications to third-party software.

## What are the features?
The use case has not been tested in server mode, outside of the local host, over TCP/IP. For example, in a scenario where a user connects within the same network from a tablet or phone to another PC with a running Lute server. In this case, in its current form, without changing the IP in the code of the FTCA utility and additional testing, it may not work. Before making this change, it is necessary to conduct a security audit of the utility and assess the risks. It is also important to remember that the exchange will take place over an unprotected HTTP channel. This allows you to read all the transmitted information between devices using regular network administrator tools.

## What inspired it?
I accidentally discovered that when making such a request `https://m.dict.cc/deutsch-russisch/test.html` to the dict.cc dictionary, after the page loads, the input field remains in focus, and the text string is highlighted as if I had entered the hotkey combination Ctrl + A to select everything in focus.

It turned out that this works with JavaScript.
Highlighted text in this way, when the focus is on this field, allows me to immediately copy it to the clipboard,
without unnecessary manipulations, and proceed with further processing. Save it, send it to another translator via
the system clipboard, etc.

## How to use Dark Mode or Dark Theme?
If you use the Chrome or Firefox browser, you have the ability to install [Dark Reader](https://github.com/darkreader/darkreader).
To configure, open a link similar to `http://127.0.0.1:5010/?clipboard=true&s=test` and enable the plugin on this site.

It should look something like this. In the screenshot, Lute and FTCA are in the default light themes, with the Dark Reader plugin enabled on them in Dark mode.
<img width="960" alt="image" src="https://github.com/user-attachments/assets/c4aabcf3-aead-41b9-bfa4-5582591a4a48" />

## What are the technical features?
When the utility is launched, a clean HTTP server is raised and a page of the dictionary adapter is published, written using HTML/JS without extensions or dependencies.

## What are the system environment prerequisites?
- Python.
- Chrome or a browser that supports the Modern Clipboard API.

## In what environment was it tested?
- Windows 11.
- Python 3.12.7.
- Chrome
Version 133.0.6943.142 (Official Build) (64-bit).
- LUTE: Learning Using Texts v3
Version: 3.10.1.

## How to configure in the Lute v3 web interface?
Settings — Languages — [German]  

Edit German  

Dictionaries — Add dictionary  
- Terms
- Pop-up window
- `http://127.0.0.1:5010/?clipboard=true&s=[LUTE]`
- Is active? = `true`

## How to allow Clipboard Read Access (Chrome)?
The script uses the Modern Clipboard API.
Which requires additional browser configuration for operation.
It is necessary to grant permission for the page to interact with the clipboard.

<img width="407" alt="{2793AAE1-85B1-4A0C-9D16-D1161511C907}" src="https://github.com/user-attachments/assets/8b0186e3-1476-46c3-afa5-f80ebb59581a" />

    Clipboard read access allowed [x]
    This site can see text and images copied to the
    clipboard.
    Continue allowing this site to see the clipboard
    Always block http://127.0.0.1:5010 from
    seeing the clipboard
    Manage Done

## How to check functionality?
Run the utility.

Go through one of the links below.  

- Option 1. Without clipboard option.
http://127.0.0.1:5010/?s=test%20test

- Option 2. With clipboard option.
http://127.0.0.1:5010/?clipboard=true&s=test

Try to change the address by entering something instead of `test`. After sending the request, press Enter, and you should see a form with a text field containing the text you entered in the request, highlighted and ready to be copied immediately. When using `clipboard=true`, provided that you have granted access to work with the clipboard on this page, you will be able to observe that this text has been automatically copied.

## What about the security of my buffer data?
When working with sensitive data, it is recommended to disable unnecessary applications and utilities that have access to it. This utility does not transmit your data outside. It does not store them on the disk, but it operates them in the RAM of your PC and transmits them over an unprotected channel between applications within your system, using the loopback network interface.
You need to assess the risks yourself. The author is open to suggestions.
I think it would also be wrong to publish this server at an address other than the loopback address, which can only expand the perimeter of attack from the outside.
In this case, the determining factor is the understanding of what materials and data you are working with in the main reading program, to which this utility is attached as an adapter.

## Why doesn't it work?
Try to kill all processes associated with this utility on your system.
Running processes can be found in the process manager.
Look for `python` and the path should contain the name of the utility `ftca`.

Make sure that the port used by the web server in this utility does not conflict with other applications that may have taken it before.

## License
MIT License.

## Author's Disclaimer
The software is provided "as is" without any warranties, either express or implied. The author is not responsible for any damages or issues arising from the use of this software. Users are advised to use it at their own risk.

## Stars
Please promote the developer's efforts by marking them with a star.
