from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

def fetch_lines_with_word(url_fetch, word_fetch):
    response = requests.get(url_fetch)
    soup = BeautifulSoup(response.text, 'html.parser')
    lines = soup.prettify().split('\n')
    filtered_lines = [line for line in lines if word_fetch in line]
    return filtered_lines

def main():
    print("=== MENU ===")
    print()
    print("1. Print HTML")
    print("2. Print 'pretty' html")
    print("3. Print XML")
    print("4. Fetch lines with word")
    print("5. Exit")

    choice = input("Your choice: ")


    if choice == '1':
        url = input("Enter URL: ")

        page = urlopen(url)

        page_b = page.read()
        html = page_b.decode("utf-8")

        print(html)

        ask_save = input("Do you want to save this output in HTML file? (y/n): ")

        if ask_save == 'y':
            text_file_name = input("Enter name for your file (it's better to add extension '.html'): ")
            text_file = open(text_file_name, "w")
            text_file.write(html)
            text_file.close()
            print("File saved successfully!")
        else:
            print("File not saved")

    elif choice == '2':
        url = input("Enter URL: ")

        page = urlopen(url)

        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        print(soup.get_text())

        ask_save = input("Do you want to save this output? (y/n): ")

        if ask_save == 'y':
            text_file_name = input("Enter name for your file (it's better to add the extension '.txt'): ")
            text_file = open(text_file_name, "w")
            text_file.write(soup.get_text())
            text_file.close()
            print("File saved successfully!")
        else:
            print("File not saved")

    elif choice == '3':
        url = input("Enter URL: ")

        response = requests.get(url)

        if response.status_code == 200:
            root = ET.fromstring(response.content)
            xml = ET.tostring(root, encoding='utf-8')
            decodedXml = xml.decode('utf-8')
            print(decodedXml)
        else:
            print(f"Error fetching data from {url}. Status code: {repsonse.status_code}")

        ask_save = input("Do you want to save this output in an XML file? (y/n): ")

        if ask_save == 'y':
            text_file_name = input("Enter name for your file (it's better to add the extension '.xml'): ")
            text_file = open(text_file_name, "w")
            text_file.write(decodedXml)
            text_file.close()
            print("File saved successfully!")
        else:
            print("File not saved")

    elif choice == '4':
        url_fetch = input("Enter URL: ")
        word_fetch = input("What word we have to find inside our html?: ")
        lines_with_word = fetch_lines_with_word(url_fetch, word_fetch)
        for line in lines_with_word:
                highlighted_line = line.replace(word_fetch, f"\033[1;31m{word_fetch}\033[0m")
                print(highlighted_line)



    elif choice == '5':
        print("Bye!")
        return

    main()

if __name__ == "__main__":
    main()
