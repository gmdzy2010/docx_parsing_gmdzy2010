import re


def element_splitting(element, context, paragraph_sep="||", style_sep="::"):
    """
    Each instance of Elements should be handled by this func, the data
    structure evolved into context as below:

    element = {
        "element_type": element_type,
        "format_name": format_name,
        "contents": [
            {
                "run_text": run_text,
                "underline": True,
                "bold": False,
            }, {
                "run_text": run_text,
                "underline": True,
                "bold": False,
            },
        ],
    }

    each element for value mapping to "contents" corresponding to the run unit
    of Microsoft Word file suffixed with docx
    """
    element_type, format_name, text = element
    contents = []
    
    # content should be formatted with context data
    try:
        content = text.format(**context)
    except KeyError:
        content = text
    
    # then content(paragraph with respect to Microsoft Word file) should be
    # split into run list with special run styles such as underline or bold
    for content_part in content.split(paragraph_sep):
        split = content_part.split(style_sep)
        
        # Style of runs depends on the template of content, so action of
        # splitting may fail, these due to a couple of plain text.
        if len(split) == 1:
            underline, bold = False, False
        else:
            underline = True if re.match('.*underline.*', split[1]) else False
            bold = True if re.match('.*bold.*', split[1]) else False
        contents.append({
            "run_text": split[0], "underline": underline, "bold": bold,
        })
    return {
        "element_type": element_type,
        "format_name": format_name,
        "contents": contents,
    }


class Elements:
    """The basic unit of content template."""
    
    def __init__(self, file_object):
        self.file_object = file_object
    
    def __iter__(self):
        while True:
            paragraph_info = self.file_object.readline().strip()
            paragraph_text = self.file_object.readline().strip()
            _ = self.file_object.readline().strip()
            if paragraph_info and paragraph_text:
                type_name, style_name = paragraph_info.split(":")
                yield type_name, style_name, paragraph_text
            else:
                break
