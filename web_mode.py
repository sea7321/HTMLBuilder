"""
file: web_mode.py
description: Understanding dataclass structures, queues, and HTML/CSS code within Python
language: Python3
author: Savannah Alfaro
"""
# Import & Set Up Workspace
import sys
import cs_queue as que
import html_turtle
import wizard_mode as wiz


# Define Variables
style_template = "style_template.txt"
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
def web_doctype(html_parts):
    """
    Adds the !DOCTYPE html tag to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :return: None
    """
    que.enqueue(html_parts, "<!DOCTYPE html>\n")


def web_head(html_parts, website_title, background_color, font_style, paragraph_color, heading_color,
             input_file, queue_of_links):
    """
    Adds the head html tag and its components in-between it (title & style) to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param website_title: the website title
    :param background_color: the background color inputted by the user
    :param font_style: the font style inputted by the user
    :param paragraph_color: the paragraph text color inputted by the user
    :param heading_color: the heading color inputted by the user
    :param input_file: the name of the text file inputted by the user (command line)
    :param queue_of_links: a queue that contains the links of each text file inputted by the user
    :return: None
    """
    que.enqueue(html_parts, "<head>\n")
    web_title(html_parts, website_title)
    if queue_of_links is not que.make_empty_queue():
        while que.is_empty(queue_of_links) is False:
            que.enqueue(html_parts, que.dequeue(queue_of_links))
    web_style(html_parts, background_color, font_style, paragraph_color, heading_color)
    que.enqueue(html_parts, "</head>\n")


def web_title(html_parts, title):
    """
    Adds the title of the website to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param title: the title of the website
    :return: None
    """
    que.enqueue(html_parts, "<h1>" + title.strip() + "</h1>\n")


def web_style(html_parts, background_color, font_style, paragraph_color, heading_color):
    """
    Reads the style template and stores each line within html_parts. Replaces the variables in the template
    with colors inputted by the user.
    :param html_parts: queue of each line of the html text file
    :param background_color: the background color inputted by the user
    :param font_style: the font style inputted by the user
    :param paragraph_color: the paragraph text color inputted by the user
    :param heading_color: the heading color inputted by the user
    :return: None
    """
    que.enqueue(html_parts, "<style>\n")
    with open(style_template) as file:
        count = 1
        line = file.readline()
        while line:
            count += 1
            if count == 28:
                break
            line = file.readline()
            line = line.replace("@BACKCOLOR", background_color)
            line = line.replace("@FONTSTYLE", font_style)
            line = line.replace("@FONTCOLOR", paragraph_color)
            line = line.replace("@HEADCOLOR", heading_color)
            que.enqueue(html_parts, line)
    que.enqueue(html_parts, "</style>\n")


def web_paragraph(html_parts, paragraph_title, paragraph_content):
    """
    Creates a paragraph using a header html tag for the title and paragraph tag for the paragraph
    content and adds it to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param paragraph_title: the title of the paragraph
    :param paragraph_content: the content of the paragraph
    :return: None
    """
    que.enqueue(html_parts, "<h2>" + str(paragraph_title) + "</h2>\n")
    que.enqueue(html_parts, "<p>" + str(paragraph_content) + "</p>\n")


def web_image(html_parts, paragraph_image):
    """
    Creates an image tag and adds it to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param paragraph_image: name of the image inputted by the user
    :return: None
    """
    que.enqueue(html_parts, "<img src=\"" + paragraph_image + "\" class=center>\n")


def web_image_percentage(html_parts, paragraph_image, image_percentage):
    """
    Creates an image tag with width and adds it to html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param paragraph_image: name of the image inputted by the user
    :param image_percentage: width percentage of the image inputted by the user
    :return: None
    """
    que.enqueue(html_parts, "<img src=\"" + paragraph_image + "\"" + " width=\""
                + image_percentage + "\"" + " class=center>\n")


def input_text_file(html_parts, input_file, background_color, font_style, paragraph_color, heading_color, queue_of_links):
    """
    Creates the body of the html file. Reads through the input_text_file and adds "commands" to
    html_parts (queue).
    :param html_parts: queue of each line of the html text file
    :param input_file: the name of the text file inputted by the user (command line)
    :param background_color: the background color inputted by the user
    :param font_style: the font style inputted by the user
    :param paragraph_color: the paragraph text color inputted by the user
    :param heading_color: the heading color inputted by the user
    :param queue_of_links: a queue that contains the links of each text file inputted by the user
    :return: (html_parts) queue of each line of the html text file
    """
    with open(input_file) as file:
        line = file.readline()
        count = 1
        while line:
            if count == 1:
                web_doctype(html_parts)
                que.enqueue(html_parts, "<html>\n")
                web_head(html_parts, line, background_color, font_style, paragraph_color, heading_color,
                         input_file, queue_of_links)
                que.enqueue(html_parts, "<body>\n")

            line = file.readline().strip()
            count += 1

            split_line = line.split()
            if line == "":
                line = file.readline().strip()
                split_line = line.split()
            if line == "!new_paragraph":
                paragraph_line = file.readline()
                paragraph_split_line = paragraph_line.split()
                paragraph_title = " ".join(paragraph_split_line[1:])
                que.enqueue(html_parts, "<h2>" + paragraph_title + "</h2>\n")
                que.enqueue(html_parts, "<p>\n")
                while paragraph_line:
                    paragraph_line = file.readline()
                    paragraph_split_line = paragraph_line.split()
                    if paragraph_line == "":
                        break
                    if paragraph_line == "\n":
                        line = paragraph_line
                        split_line = paragraph_line.split()
                        break
                    elif paragraph_split_line[0] == "!image":
                        split_line = paragraph_split_line
                        break
                    que.enqueue(html_parts, paragraph_line)
                que.enqueue(html_parts, "</p>\n")
            if len(split_line) > 0 and split_line[0] == "!image":
                if len(split_line) == 2:
                    web_image(html_parts, split_line[1])
                elif len(split_line) == 3:
                    web_image_percentage(html_parts, split_line[1], split_line[2])
                else:
                    raise Exception("Incorrect format for image command.")

        que.enqueue(html_parts, "</body>\n")
        que.enqueue(html_parts, "</html>\n")

    return html_parts


def output_text_file(queue, count):
    """
    Outputs a html text file with the specified file name.
    :param queue: (html_parts) queue of each line of the html text file
    :param count: the number of files inputted by the user through command line
    :return: None
    """
    with open(get_title(sys.argv[count]) + ".html", "w+") as file:
        while que.is_empty(queue) is False:
            file.writelines(que.dequeue(queue))


def get_title(input_file):
    """
    Returns the title of the website of a given input_file.
    :param input_file: the name of the text file inputted by the user (command line)
    :return: (line) title of the website
    """
    with open(input_file) as file:
        line = file.readline().strip()
    return line


def link_queue():
    """
    Returns a queue of links of website titles that were inputted by the user through command line.
    :return: (queue_of_links) a queue that contains the links of each text file inputted by the user
    """
    # Make New Queue for Links
    queue_of_links = que.make_empty_queue()

    count = len(sys.argv) - 1
    while count >= 1:
        que.enqueue(queue_of_links, "<a href=\"" + get_title(sys.argv[count]) + ".html\">" + get_title(sys.argv[count])
                    + "</a>\n")
        count -= 1
    return queue_of_links


def web_mode():
    """
    Makes the queue for html_parts, asks for user input for colors and text style, and
    makes html files with links for each input file given.
    :return: None
    """
    # Make New Queue for HTML parts
    html_parts = que.make_empty_queue()
    count = len(sys.argv) - 1

    # User Input
    background_color = wiz.color_background()

    font_style = wiz.font_choice()

    paragraph_color = wiz.color_paragraph()

    heading_color = wiz.color_heading()

    # Make html files for each input_file
    if count == 1:
        input_file = sys.argv[count]
        queue_of_links = que.make_empty_queue()
        output_text_file(input_text_file(html_parts, input_file, background_color, font_style, paragraph_color,
                                         heading_color, queue_of_links), count)
        print("\nYour HTML file has been saved.")
    else:
        while count >= 1:
            input_file = sys.argv[count]
            queue_of_links = link_queue()
            output_text_file(input_text_file(html_parts, input_file, background_color, font_style, paragraph_color,
                             heading_color, queue_of_links), count)
            count -= 1
        print("\nYour HTML file has been saved.")

