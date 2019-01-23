from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt

from docx_parsing_gmdzy2010.utilities import Price2UpperChinese


PARAGRAPH_CONTEXT = {
    "demo_field_1": Price2UpperChinese(21000.00),
    "demo_field_2": 300.00,
    "demo_field_3": 18003.00,
    "demo_field_4": Price2UpperChinese(18003.00),
    "demo_field_5": 100,
    "demo_field_6": 1000.00,
    "demo_field_7": Price2UpperChinese(1000.00),
    "demo_field_8": 100,
    "demo_field_9": "测试文本测试文本测试文本",
    "demo_field_10": "测试文本测试文本测试文本",
    "demo_field_11": "测试文本测试文本测试文本",
    "demo_field_12": "测试文本测试文本测试文本测试文本测试文本",
}

PARAGRAPH_FORMAT = {
    "cover_title": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.CENTER,
        "space_before": Pt(90),
        "space_after": Pt(90),
    },
    "cover_info": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "space_before": Pt(18),
        "space_after": Pt(18),
    },
    "vice_cover_title": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.CENTER,
        "space_before": Pt(90),
        "space_after": Pt(90),
        "page_break_before": True,
    },
    "vice_cover_info": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
    },
    "vice_cover_info_space": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "space_after": Pt(48),
    },
    "body_normal": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.JUSTIFY,
        "first_line_indent": Pt(24),
    },
    "body_normal_break": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.JUSTIFY,
        "space_before": Pt(12),
        "space_after": Pt(12),
        "page_break_before": True,
        "first_line_indent": Pt(24),
    },
    "body_heading_1": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "space_before": Pt(18),
        "space_after": Pt(12),
    },
    "body_heading_1_space": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "space_before": Pt(48),
        "space_after": Pt(48),
    },
    "body_heading_2": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
    },
    "body_heading_3": {
        "alignment": WD_PARAGRAPH_ALIGNMENT.LEFT,
        "first_line_indent": Pt(24),
    },
}

TABLE_CONTEXT = {
    "demo_table_1": {
        "attr": {
            "style": "Table Grid",
            "row": 1,
            "column": 4,
        },
        "data": (
            ("第1列标题", "第2列标题", "第3列标题", "第4列标题"),
            ("第1行第1列内容", "第1行第2列内容", "第1行第3列内容", "第1行第4列内容"),
            ("第2行第1列内容", "第2行第2列内容", "第2行第3列内容", "第2行第4列内容"),
            ("第3行第1列内容", "第3行第2列内容", "第3行第3列内容", "第3行第4列内容"),
            ("第4行第1列内容", "第4行第2列内容", "第4行第3列内容", "第4行第4列内容"),
        )

    },
},

PICTURE_CONTEXT = {
    "demo_table_1": {
        "width": 320,
        "height": 240,
    },
},
