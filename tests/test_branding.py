"""Static brand regressions; browser/layout checks are separate release gates."""
from html.parser import HTMLParser
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]


class Tags(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.metas = {}
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "meta":
            self.metas[attrs.get("property", attrs.get("name"))] = attrs.get("content")


class BrandingTests(unittest.TestCase):
    def test_homepage_identity_and_tagline(self):
        text = (ROOT / "index.html").read_text()
        self.assertIn('class="logo"', text)
        self.assertIn('>Beyond AI</a>', text)
        self.assertIn('<h1>Architecting <em>the Future</em></h1>', text)
        self.assertIn('publish the numbers that hurt', text)
        meta = Tags(text).metas
        self.assertEqual(meta['og:title'], 'Beyond AI — Architecting the Future | Idan Shimon')
        self.assertEqual(meta['og:url'], 'https://idanshimon.github.io/')
        self.assertEqual(meta['og:image'], 'https://idanshimon.github.io/assets/og-home.png')

    def test_publication_labels_are_current(self):
        pages = sorted(ROOT.rglob('*.html'))
        self.assertTrue(pages)
        for page in pages:
            with self.subTest(page=str(page.relative_to(ROOT))):
                text = page.read_text()
                self.assertNotIn('Ground Truth', text)
                self.assertEqual(Tags(text).metas.get('og:site_name'), 'Beyond AI')

    def test_shared_monogram(self):
        icon = ET.fromstring((ROOT / 'assets/favicon.svg').read_text())
        labels = [node.text for node in icon.iter() if node.tag.endswith('}text')]
        self.assertEqual(labels, ['BA'])

    def test_home_preview_source(self):
        text = (ROOT / 'assets/og-home.html').read_text()
        self.assertIn('Beyond AI', text)
        self.assertIn('Architecting<br><em>the Future</em>', text)
        self.assertNotIn('Ground Truth', text)
        self.assertTrue((ROOT / 'assets/og-home.png').is_file())


if __name__ == '__main__':
    unittest.main()
