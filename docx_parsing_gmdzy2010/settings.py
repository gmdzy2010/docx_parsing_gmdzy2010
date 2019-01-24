from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.shared import Pt


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
