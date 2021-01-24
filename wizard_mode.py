"""
file: wizard_mode.py
description: Understanding dataclass structures, queues, and HTML/CSS code within Python
language: Python3
author: Savannah Alfaro
"""
# Import & Set Up Workspace
import web_mode as web
import cs_queue as que
import html_tu

# Define Variables
list_colors = ['peachpuff', 'slateblue', 'powderblue', 'lightcyan', 'chartreuse', 'moccasin', 'mediumseagreen',
               'lawngreen', 'seagreen', 'mintcream', 'azure', 'goldenrod', 'lightblue', 'firebrick', 'lightseagreen',
               'chocolate', 'yellowgreen', 'darkolivegreen', 'violet', 'ivory', 'sandybrown', 'wheat', 'mediumvioletred',
               'bisque', 'lightgreen', 'cyan', 'hotpink', 'gray', 'indianred ', 'antiquewhite', 'royalblue', 'yellow',
               'indigo ', 'lightcoral', 'darkslategrey', 'sienna', 'lightslategray', 'mediumblue', 'red', 'khaki',
               'darkviolet', 'mediumorchid', 'darkblue', 'lightskyblue', 'turquoise', 'lightyellow', 'grey',
               'whitesmoke', 'blueviolet', 'orchid', 'mediumslateblue', 'darkturquoise', 'coral', 'forestgreen',
               'gainsboro', 'darkorange', 'cornflowerblue', 'lightsteelblue', 'plum', 'lavender', 'palegreen', 'darkred',
               'dimgray', 'floralwhite', 'orangered', 'oldlace', 'darksalmon', 'lavenderblush', 'darkslategray', 'tan',
               'cadetblue', 'silver', 'tomato', 'darkkhaki', 'slategray', 'maroon', 'olive', 'deeppink', 'linen',
               'magenta', 'crimson', 'mistyrose', 'lime', 'saddlebrown', 'blanchedalmond', 'black', 'snow', 'seashell',
               'darkcyan', 'gold', 'midnightblue', 'darkgoldenrod', 'palevioletred', 'fuchsia', 'teal', 'lightpink',
               'darkgrey', 'mediumspringgreen', 'aquamarine', 'lightsalmon', 'navajowhite', 'darkgreen', 'burlywood',
               'rosybrown', 'springgreen', 'purple', 'olivedrab', 'lightslategrey', 'orange', 'aliceblue',
               'mediumaquamarine', 'navy', 'salmon', 'rebeccapurple', 'darkmagenta', 'limegreen', 'deepskyblue', 'pink',
               'mediumpurple', 'skyblue', 'aqua', 'blue', 'slategrey', 'darkslateblue', 'honeydew', 'darkseagreen',
               'paleturquoise', 'brown', 'thistle', 'lemonchiffon', 'peru', 'cornsilk', 'papayawhip', 'green',
               'lightgoldenrodyellow', 'mediumturquoise', 'steelblue', 'lightgray', 'lightgrey', 'beige', 'palegoldenrod',
               'darkgray', 'white', 'ghostwhite', 'dodgerblue', 'greenyellow', 'dimgrey', 'darkorchid']


# Define Functions
def wizard_head(html_parts, website_title, background_color, font_style, paragraph_color, heading_color):
    """
    Adds the head html tag and its components in-between it (title & style) to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param website_title: the website title
    :param background_color: the background color inputted by the user
    :param font_style: the font style inputted by the user
    :param paragraph_color: the paragraph text color inputted by the user
    :param heading_color: the heading color inputted by the user
    :return: None
    """
    que.enqueue(html_parts, "<head>\n")
    web.web_title(html_parts, website_title)
    web.web_style(html_parts, background_color, font_style, paragraph_color, heading_color)
    que.enqueue(html_parts, "</head>\n")


def wizard_body(html_parts):
    """
    Adds the body html tag and its components in-between it (paragraph & paragraph title) to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :return: None
    """
    que.enqueue(html_parts, "<body>\n")
    wizard_paragraph(html_parts)
    que.enqueue(html_parts, "</body>\n")


def wizard_html(html_parts, website_title, background_color, font_style, paragraph_color, heading_color):
    """
    Adds the html html tag and its components in-between it (head and body) to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param website_title: the website title
    :param background_color: the background color inputted by the user
    :param font_style: the font style inputted by the user
    :param paragraph_color: the paragraph text color inputted by the user
    :param heading_color: the heading color inputted by the user
    :return: None
    """
    que.enqueue(html_parts, "<html>\n")
    wizard_head(html_parts, website_title, background_color, font_style, paragraph_color, heading_color)
    wizard_body(html_parts)
    que.enqueue(html_parts, "</html>\n")


def wizard_paragraph(html_parts):
    """
    Creates a paragraph html tag and adds it to html_parts (queue). Asks for user input when
    adding images and multiple paragraphs.
    :param html_parts: queue of each line of the html text file
    :return: None
    """
    paragraph_title = input("Title of your paragraph: ")
    paragraph_content = input("Content of your paragraph (single line): ")
    web.web_paragraph(html_parts, paragraph_title, paragraph_content)

    answer_image = input("Do you want to add images? [yes] ")
    if answer_image == "yes" or "":
        paragraph_image = input("Image file name: ")
        web.web_image(html_parts, paragraph_image)
        answer_image2 = input("Do you want to add another image? [yes] ")
        while answer_image2 == "yes" or "":
            paragraph_image = input("Image file name: ")
            web.web_image(html_parts, paragraph_image)
            answer_image2 = input("Do you want to add another image? [yes] ")

    answer_paragraph = input("Do you want to add another paragraph to your website? [yes] ")
    if answer_paragraph == "yes" or "":
        wizard_paragraph(html_parts)


def wizard_output_text_file(queue):
    """
    Outputs a html text file with the specified file name.
    :param queue: (html_parts) queue of each line of the html text file
    :return: None
    """
    with open("index.html", "w+") as file:
        while que.is_empty(queue) is False:
            file.writelines(que.dequeue(queue))


def color_background():
    """
    Checks to see if the color inputted by the user is acceptable within the list (list_colors).
    :return: (background color) the background color inputted by the user
    """
    print("Background Color")
    background_color = input("Choose the name of a color, or in format '#XXXXXX': ")
    if background_color[0] == "#" and len(background_color) == 7:
        return background_color
    elif (background_color in list_colors) is True:
        return background_color
    else:
        return color_background()


def font_choice():
    print("You will now choose a font.")
    answer_fonts = input("Do you want to see what the fonts look like? [yes] ")
    if answer_fonts == "yes" or "":
        html_turtle.draw_textbox()
    font_number = input("0: Arial, size 16\n"
                        "1: Comic Sans MS, size 16\n"
                        "2: Lucida Grande, size 16\n"
                        "3: Tahoma, size 16\n"
                        "4: Verdana, size 16\n"
                        "5: Helvetica, size 16\n"
                        "6: Times New Roman, size 16\n"
                        "Choose a font by its number: ")

    font_style = ""
    if font_number == str(0):
        return "Arial"
    elif font_number == str(1):
        return "Comic Sans MS"
    elif font_number == str(2):
        return "Lucida Grande"
    elif font_number == str(3):
        return "Tahoma"
    elif font_number == str(4):
        return "Verdana"
    elif font_number == str(5):
        return "Helvetica"
    elif font_number == str(6):
        return "Times New Roman"
    else:
        print("Please input a number to represent a font.")
        return font_choice()


def color_paragraph():
    """
    Checks to see if the color inputted by the user is acceptable within the list (list_colors).
    :return: (paragraph_color) the paragraph text color inputted by the user
    """
    print("Paragraph Text Color")
    paragraph_color = input("Choose the name of a color, or in format '#XXXXXX': ")
    if paragraph_color[0] == "#" and len(paragraph_color) == 7:
        return paragraph_color
    elif (paragraph_color in list_colors) is True:
        return paragraph_color
    else:
        return color_paragraph()


def color_heading():
    """
    Checks to see if the color inputted by the user is acceptable within the list (list_colors).
    :return: (heading_color) the heading color inputted by the user
    """
    print("Heading Color")
    heading_color = input("Choose the name of a color, or in format '#XXXXXX': ")
    if heading_color[0] == "#" and len(heading_color) == 7:
        return heading_color
    elif (heading_color in list_colors) is True:
        return heading_color
    else:
        return color_heading()


def wizard_mode():
    """
    Makes the queue for html_parts, asks for user input for colors and text style, and
    makes html file with the variables inputted by the user.
    :return: None
    """
    # Make New Queue for HTML parts
    html_parts = que.make_empty_queue()

    # User Input
    website_title = input("What is the title of your website?: ")

    background_color = color_background()

    font_style = font_choice()

    paragraph_color = color_paragraph()

    heading_color = color_heading()

    web.web_doctype(html_parts)
    wizard_html(html_parts, website_title, background_color, font_style, paragraph_color, heading_color)
    wizard_output_text_file(html_parts)

    print("\nYour HTML file has been saved as index.html")
