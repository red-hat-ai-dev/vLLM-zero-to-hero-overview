"""Offline checks for local documentation references and SVG XML."""

from html.parser import HTMLParser
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        self.links.extend(
            value for key, value in attrs if key in ("src", "href") and value
        )


class DocumentationTests(unittest.TestCase):
    def test_local_links(self):
        documents = list(ROOT.glob("*.md")) + list(ROOT.glob("llm-d/*.md"))
        for path in documents:
            source = path.read_text()
            parser = Links()
            parser.feed(source)
            links = re.findall(r"!?\[[^\]]*\]\(([^)]+)\)", source) + parser.links
            for target in links:
                parsed = urlsplit(target.strip("<>"))
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                with self.subTest(document=path.name, target=target):
                    self.assertTrue((path.parent / unquote(parsed.path)).exists())

    def test_svg_xml(self):
        for directory in (ROOT / "assets", ROOT / "llm-d/assets"):
            for path in directory.glob("*.svg"):
                with self.subTest(svg=path.name):
                    self.assertEqual(
                        ET.parse(path).getroot().tag, "{http://www.w3.org/2000/svg}svg"
                    )


if __name__ == "__main__":
    unittest.main()
