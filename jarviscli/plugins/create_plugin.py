import os
from colorama import Fore
from plugin import plugin, require, MACOS, LINUX
"""This plugin is developed for developers as its use is to create a template
based on the guidlines of the creators of the project
to ecourage people to experiment with jarvis's plugins.
"""


@require(platform=MACOS)
@plugin("create plugin")
def create_plugin_MAC(jarvis, s):
    """The os.path method is used to track the path in which this plugin is stored
    and locate the Jarvis/custom folder through relative pathing.
    """
    path = os.path.abspath(__file__)
    plugins_path = os.path.dirname(path)
    custom_plugins_path = os.path.join(plugins_path, '..', '..', 'custom/')

    # Jarvis asks for the name of the plugin to create if not provided.

    if s == "":
        jarvis.say("Please insert the name of your plugin: ", Fore.RED)
        name = jarvis.input()
    else:
        name = s
    """The name fillters through the format_file name
    which converts it to a valid filename.
    """
    filename = format_filename(name)
    # Flag to terminate process
    exit = False
    """Checks if file already exists in either the plugins main folder
    or in the custom plugins folder and also asks the user if he wants to exit
    """
    while(os.path.isfile(custom_plugins_path + filename + ".py") or
          os.path.isfile(plugins_path + "/" + filename + ".py") and not exit):
        jarvis.say("A plugin with the name '" + filename + "' already exists", Fore.RED)
        jarvis.say("Please choose another name or type 'exit' for obvious results:", Fore.CYAN)

        new_name = jarvis.input()
        if new_name == 'exit':
            exit = True
        filename = format_filename(new_name)
    if(not exit):
        """The templated is generated through the create_template funcion
        and is exceuted through the os.system method.
        """
        string = create_template(custom_plugins_path, filename)
        os.system(string)

        if os.path.isfile(custom_plugins_path + filename + ".py"):
            jarvis.say(filename + ".py created successfully inside Jarvis/custom",
                       Fore.CYAN)
            string = "open " + custom_plugins_path + filename + ".py"
            os.system(string)
        else:
            jarvis.say("Something went wrong in the creation of the plugin :(",
                       Fore.RED)



@require(platform=LINUX)
@plugin("create plugin")
def create_plugin_LINUX(jarvis, s):
    """The os.path method is used to track the path in which this plugin is stored
    and locate the Jarvis/custom folder through relative pathing.
    """
    path = os.path.abspath(__file__)
    plugins_path = os.path.dirname(path)
    custom_plugins_path = os.path.join(plugins_path, '..', '..', 'custom/')

    # Jarvis asks for the name of the plugin to create if not provided.

    if s == "":
        jarvis.say("Please insert the name of your plugin: ", Fore.RED)
        name = jarvis.input()
    else:
        name = s
    """The name fillters through the format_file name
    which converts it to a valid filename.
    """
    filename = format_filename(name)
    # Flag to terminate process
    exit = False
    """Checks if file already exists in either the plugins main folder
    or in the custom plugins folder and also asks the user if he wants to exit
    """
    while(os.path.isfile(custom_plugins_path + filename + ".py") or
          os.path.isfile(plugins_path + "/" + filename + ".py") and not exit):
        jarvis.say("A plugin with the name '" + filename + "' already exists", Fore.RED)
        jarvis.say("Please choose another name or type 'exit' for obvious results:", Fore.CYAN)

        new_name = jarvis.input()
        if new_name == 'exit':
            exit = True
        filename = format_filename(new_name)
    if(not exit):
        """The plugin is created through the Terminal command "cat"
        and excecuted with the os.System method.
        """
        string = """cd """ + custom_plugins_path + """
            cat >> """ + filename + """.py << EOL
# All plugins should inherite from this library
from plugin import plugin

# This is the standard form of a plugin for jarvis

# Anytime you make a change REMEMBER TO RESTART Jarvis

# You can run it through jarvis by the name
# in the @plugin tag.


@plugin("my plugin")
def my_plugin(jarvis, s):

    # Prints 'This is my new plugin!'
    jarvis.say("This is my new plugin!")

# For more info about plugin development visit:
# https://github.com/sukeesh/Jarvis/blob/master/doc/PLUGINS.md
EOL"""
        os.system(string)
        if os.path.isfile(custom_plugins_path + filename + ".py"):
            jarvis.say(filename + ".py created successfully inside Jarvis/custom",
                       Fore.CYAN)
            string = "xdg-open " + custom_plugins_path + filename + ".py"
            os.system(string)
        else:
            jarvis.say("Something went wrong in the creation of the plugin :(",
                       Fore.RED)


def format_filename(name):
    """Take a string and return a valid filename constructed from the string.
Uses a whitelist approach: any characters not present in valid_chars are
removed. Also spaces are replaced with underscores.

Note: this method may produce invalid filenames such as ``, `.` or `..`
When I use this method I prepend a date string like '2009_01_15_19_46_32_'
and append a file extension like '.txt', so I avoid the potential of using
an invalid filename.

"""
    import string

    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    filename = ''.join(c for c in name if c in valid_chars)
    filename = filename.replace(' ', '_')  # I don't like spaces in filenames.
    return filename

"""This method is used to format the template of the plugin
that is being created given the filename and the path
in which it will be stored.
"""
def create_template(custom_plugins_path, filename):

	template = """cd """ + custom_plugins_path + """
            cat >> """ + filename + """.py << EOL
# All plugins should inherite from this library
from plugin import plugin

# This is the standard form of a plugin for jarvis

# Anytime you make a change REMEMBER TO RESTART Jarvis

# You can run it through jarvis by the name
# in the @plugin tag.


@plugin("my plugin")
def my_plugin(jarvis, s):

    # Prints 'This is my new plugin!'
    jarvis.say("This is my new plugin!")

# For more info about plugin development visit:
# https://github.com/sukeesh/Jarvis/blob/master/doc/PLUGINS.md
EOL"""

	return template