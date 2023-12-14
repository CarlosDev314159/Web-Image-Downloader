import os
import requests
import PySimpleGUI as sg
from termcolor import colored
import random
import sys


# List of user agents to choose from randomly
user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.1 Safari/603.1.30",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 OPR/44.0.2510.1449",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 Vivaldi/1.9.818.44",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/45.0.2552.635",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 Vivaldi/1.9.818.44",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36 OPR/44.0.2510.1449"
]


def show_message(message):
    return sg.popup(message)


def download_image(link, path):
    try:
        show_message(f"Downloading {link}")
        response = requests.get(
            link, headers={'User-Agent': random.choice(user_agents)})
        if response.status_code == 200:
            with open(os.path.join(path, os.path.basename(link)), 'wb') as file:
                file.write(response.content)
            show_message(f"Downloaded {link} with success in {path}")
        else:
            show_message(
                f"Download failed!\nStatus code: {response.status_code}")
    except Exception as e:
        show_message("Download failed!")
        show_message(f"ERROR LOG: {e}")


def main():
    images = []

    layout = [
        [sg.Text("Enter the image URL.")],
        [sg.Input(key='-IN-')],
        [sg.Button('OK'), sg.Button('Exit'), sg.Button('Download All')],
    ]

    window = sg.Window('Image Downloader', layout)

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event == 'OK':
            url = values['-IN-']
            if url == "0":
                break
            elif url != "1" and url != "":
                show_message(f"Added {url} to the list.")
                images.append(url)
                window['-IN-'].update('')
            elif url == "1" and len(images) == 0:
                show_message("No URL provided! Try again.")
            elif url == "":
                show_message("No URL provided! Try again.")
            elif url == "1" and len(images) > 0:
                path = sg.popup_get_folder('Where would you like to save?')
                if path:
                    os.chdir(path)
                    for image in images:
                        download_image(image, path)
                else:
                    show_message("No directory selected!")
                    break
        elif event == 'Download All' and len(images) == 0:
            show_message("No URL provided! Try again.")
        elif event == 'Download All' and len(images) > 0 and url != "":
            path = sg.popup_get_folder('Where would you like to save?')
            if path:
                os.chdir(path)
                for image in images:
                    download_image(image, path)
            else:
                show_message("No directory selected!")
                break

    window.close()


if __name__ == "__main__":
    main()
