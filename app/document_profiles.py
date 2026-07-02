from __future__ import annotations

import re
from typing import Dict, Any, List

DOC_PROFILES: Dict[str, Dict[str, Any]] = {
    "novel": {
        "label": "Novel",
        "mode": "novel",
        "category": "literary",
        "default_theme": "classic_cream",
        "fonts": {"title": "Cormorant Garamond", "heading": "Cormorant Garamond", "subheading": "Cormorant Garamond", "body": "EB Garamond", "caption": "EB Garamond", "mono": "JetBrains Mono", "quote": "Cormorant Garamond"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "page_break", "section_divider", "epigraph", "part_division", "chapter_opener", "figure", "image_caption", "glossary", "timeline_appendix", "bibliography", "appendix", "footnote", "author_note", "interlude", "flashback_marker", "manuscript_header", "dedication"],
        "disallowed_blocks": ["table", "chart", "risk_matrix", "swot_matrix", "comparison_matrix"],
        "content_rules": ["No tables by default.", "No corporate styling.", "Keep prose immersive and scene-driven."],
    },
    "narrative_nonfiction": {
        "label": "Narrative Non-Fiction",
        "mode": "novel",
        "category": "literary",
        "default_theme": "classic_cream",
        "fonts": {"title": "Playfair Display", "heading": "Cormorant Garamond", "subheading": "Cormorant Garamond", "body": "Lora", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Cormorant Garamond"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "page_break", "section_divider", "epigraph", "chapter_opener", "figure", "image_caption", "timeline_appendix", "bibliography", "footnote", "appendix", "author_note"],
        "disallowed_blocks": ["table", "chart", "risk_matrix", "swot_matrix", "comparison_matrix"],
        "content_rules": ["Prose must read as immersive narrative, not academic writing.", "Footnotes and bibliography allowed in appendix only.", "No corporate report styling."],
    },
    "short_story_collection": {
        "label": "Short Story Collection",
        "mode": "short_story",
        "category": "literary",
        "default_theme": "classic_cream",
        "fonts": {"title": "Playfair Display", "heading": "Cormorant Garamond", "subheading": "Cormorant Garamond", "body": "EB Garamond", "caption": "EB Garamond", "mono": "JetBrains Mono", "quote": "Cormorant Garamond"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "page_break", "section_divider", "story_title_page", "author_note", "figure", "image_caption", "interlude", "dedication", "epigraph"],
        "disallowed_blocks": ["table", "chart", "risk_matrix", "swot_matrix", "comparison_matrix"],
        "content_rules": ["No tables unless explicitly requested.", "Preserve independent story endings."],
    },
    "poetry_collection": {
        "label": "Poetry Collection",
        "mode": "poetry",
        "category": "literary",
        "default_theme": "rose_poetics",
        "fonts": {"title": "Playfair Display", "heading": "Cormorant Garamond", "subheading": "Cormorant Garamond", "body": "Crimson Text", "caption": "Crimson Text", "mono": "JetBrains Mono", "quote": "Crimson Text"},
        "allowed_blocks": ["paragraph", "poem", "heading", "quote", "page_break", "section_divider", "epigraph", "dedication", "figure", "image_caption", "poet_note", "translator_note", "form_label"],
        "disallowed_blocks": ["table", "chart", "risk_matrix", "swot_matrix", "comparison_matrix"],
        "content_rules": ["Centered poem layout.", "Wide whitespace.", "No justified paragraphs.", "No tables."],
    },
    "executive_report": {
        "label": "Executive Report",
        "mode": "report",
        "category": "report",
        "default_theme": "modern_corporate",
        "fonts": {"title": "Inter", "heading": "Inter", "subheading": "Inter", "body": "Source Sans 3", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Source Sans 3"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "table", "chart", "timeline", "risk_matrix", "swot_matrix", "comparison_matrix", "kpi_cards", "callout_box", "note_box", "warning_box", "tip_box", "figure", "image_caption", "equation", "footnote", "appendix", "glossary", "bibliography", "page_break", "section_divider", "source_notes", "section_numbering"],
        "disallowed_blocks": [],
        "content_rules": ["Use tables, charts, risk matrices, timelines, KPI cards, and callouts when useful.", "Use structured JSON blocks instead of raw Markdown when a visual block is needed.", "Lock fonts, colors, and layout for the whole PDF."],
    },
    "cyber_threat_intelligence_report": {
        "label": "Cyber Threat Intelligence Report",
        "mode": "report",
        "category": "report",
        "default_theme": "tactical_dark",
        "fonts": {"title": "Rajdhani", "heading": "IBM Plex Sans Condensed", "subheading": "IBM Plex Sans Condensed", "body": "IBM Plex Sans", "caption": "IBM Plex Sans", "mono": "JetBrains Mono", "quote": "IBM Plex Sans"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "table", "chart", "timeline", "risk_matrix", "comparison_matrix", "ioc_table", "cve_table", "mitre_table", "kill_chain_diagram", "severity_badge", "analyst_notes", "code_block", "sigma_rule_block", "yara_rule_block", "network_diagram", "timeline_chart", "heatmap", "stix_object_table", "appendix", "figure", "image_caption", "source_notes", "page_break"],
        "disallowed_blocks": [],
        "content_rules": ["Include IOC, CVE, and MITRE ATT&CK tables where relevant.", "Support kill-chain diagrams, timeline charts, and analyst notes.", "Allow YARA/Sigma/code blocks in appendices."],
    },
    "technical_manual": {
        "label": "Technical Manual",
        "mode": "report",
        "category": "report",
        "default_theme": "minimal_mono",
        "fonts": {"title": "IBM Plex Sans", "heading": "IBM Plex Sans", "subheading": "IBM Plex Sans", "body": "Source Sans 3", "caption": "Source Sans 3", "mono": "Fira Code", "quote": "Source Sans 3"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "code_block", "command_block", "warning_box", "note_box", "tip_box", "table", "diagram", "figure", "image_caption", "page_break", "section_divider", "step_list", "api_reference", "parameter_table", "troubleshooting", "faq", "changelog", "appendix", "architecture_diagram", "decision_tree", "environment_table", "dependency_table", "release_notes"],
        "disallowed_blocks": [],
        "content_rules": ["Use step-by-step sections, code blocks, command boxes, and warning boxes.", "Keep parameter tables clean and aligned."],
    },
    "academic_paper": {
        "label": "Academic Paper",
        "mode": "report",
        "category": "report",
        "default_theme": "minimal_mono",
        "fonts": {"title": "Libertinus Serif", "heading": "Libertinus Serif", "subheading": "Libertinus Serif", "body": "Libertinus Serif", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Libertinus Serif"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "figure", "image_caption", "equation", "footnote", "bibliography", "table", "section_numbering", "references", "appendix", "page_break", "caption", "callout_box", "abstract_block", "author_affiliation", "doi_block", "theorem_block", "proof_block", "algorithm_block"],
        "disallowed_blocks": [],
        "content_rules": ["Support section numbering, captions, tables, equations, footnotes, and bibliography."],
    },
    "business_proposal": {
        "label": "Business Proposal",
        "mode": "report",
        "category": "report",
        "default_theme": "modern_corporate",
        "fonts": {"title": "Inter", "heading": "Manrope", "subheading": "Manrope", "body": "Source Sans 3", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Source Sans 3"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "pricing_table", "timeline_chart", "deliverable_cards", "comparison_table", "signature_page", "callout_box", "appendix", "page_break", "figure", "cover_page", "executive_summary_block", "team_bios", "case_study_block", "testimonial_block"],
        "disallowed_blocks": [],
        "content_rules": ["Use pricing tables, timeline charts, deliverable cards, and comparison tables."],
    },
    "market_research_report": {
        "label": "Market Research Report",
        "mode": "report",
        "category": "report",
        "default_theme": "modern_corporate",
        "fonts": {"title": "Manrope", "heading": "Inter", "subheading": "Inter", "body": "Source Sans 3", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Source Sans 3"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "bar_chart", "pie_chart", "donut_chart", "competitor_table", "swot_matrix", "persona_cards", "market_sizing_table", "risk_matrix", "appendix", "page_break", "figure", "image_caption", "heat_map", "funnel_chart", "cohort_table", "trend_line_chart", "survey_results_table"],
        "disallowed_blocks": [],
        "content_rules": ["Use bar charts, pie charts, competitor tables, SWOT matrices, persona cards, and market sizing tables."],
    },
    "legal_brief": {
        "label": "Legal Brief / Memorandum",
        "mode": "report",
        "category": "report",
        "default_theme": "minimal_mono",
        "fonts": {"title": "Libertinus Serif", "heading": "Libertinus Serif", "subheading": "Libertinus Serif", "body": "Libertinus Serif", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Libertinus Serif"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "table", "footnote", "bibliography", "references", "appendix", "page_break", "section_divider", "callout_box", "section_numbering"],
        "disallowed_blocks": ["chart", "risk_matrix", "swot_matrix", "pie_chart", "bar_chart"],
        "content_rules": ["Use formal legal register throughout.", "Section numbering is mandatory.", "No charts or visual matrices.", "Footnotes and references are first-class elements."],
    },
    "incident_response_report": {
        "label": "Incident Response Report",
        "mode": "report",
        "category": "report",
        "default_theme": "minimal_mono",
        "fonts": {"title": "Rajdhani", "heading": "IBM Plex Sans Condensed", "subheading": "IBM Plex Sans Condensed", "body": "IBM Plex Sans", "caption": "IBM Plex Sans", "mono": "JetBrains Mono", "quote": "IBM Plex Sans"},
        "allowed_blocks": ["paragraph", "heading", "bullet_list", "numbered_list", "timeline_chart", "severity_badge", "ioc_table", "cve_table", "analyst_notes", "code_block", "kill_chain_diagram", "action_items_table", "remediation_table", "appendix", "figure", "image_caption", "source_notes", "page_break", "executive_summary_block", "lessons_learned_block"],
        "disallowed_blocks": [],
        "content_rules": ["Lead with an executive summary block.", "Timeline chart required for attack chronology.", "IOC and remediation tables must be present.", "Lessons-learned block at the end."],
    },
    "investment_memo": {
        "label": "Investment Memo",
        "mode": "report",
        "category": "report",
        "default_theme": "modern_corporate",
        "fonts": {"title": "Manrope", "heading": "Inter", "subheading": "Inter", "body": "Source Sans 3", "caption": "Source Sans 3", "mono": "JetBrains Mono", "quote": "Lora"},
        "allowed_blocks": ["paragraph", "heading", "quote", "bullet_list", "numbered_list", "table", "bar_chart", "line_chart", "donut_chart", "kpi_cards", "risk_matrix", "comparison_matrix", "callout_box", "warning_box", "timeline", "appendix", "page_break", "figure", "image_caption", "source_notes"],
        "disallowed_blocks": [],
        "content_rules": ["Use KPI cards for key financial metrics.", "Include risk matrix where thesis risks are discussed.", "Bar and line charts preferred for financial projections.", "No legal or academic register."],
    },
}

MODE_TO_DEFAULT_DOC_TYPE = {"novel": "novel", "short_story": "short_story_collection", "poetry": "poetry_collection", "report": "executive_report"}

REPORT_DOC_TYPES = ["executive_report", "cyber_threat_intelligence_report", "technical_manual", "academic_paper", "business_proposal", "market_research_report", "legal_brief", "incident_response_report", "investment_memo"]

DOC_TYPE_KEYWORDS: Dict[str, List[str]] = {
    "cyber_threat_intelligence_report": ["mitre", "ioc", "indicator of compromise", "yara", "sigma", "threat actor", "cve", "malware", "kill chain", "att&ck", "cti", "campaign", "intrusion set", "apt", "ransomware", "phishing", "c2", "command and control", "ttp", "tactics techniques", "siem", "soc", "threat hunting", "vulnerability", "exploit", "payload", "persistence", "lateral movement", "exfiltration", "detection rule"],
    "technical_manual": ["installation", "configuration", "api reference", "parameters", "troubleshooting", "commands", "manual", "how to use", "step-by-step", "faq", "changelog", "setup guide", "quickstart", "deployment", "architecture", "system requirements", "cli", "environment variable", "docker", "kubernetes", "integration"],
    "academic_paper": ["abstract", "keywords", "literature review", "methodology", "results", "discussion", "references", "bibliography", "citations", "equation", "hypothesis", "experiment", "dataset", "findings", "conclusion", "related work", "future work", "peer review", "journal", "conference paper", "preprint"],
    "business_proposal": ["proposal", "pricing", "scope of work", "deliverables", "signature", "timeline", "team", "terms", "closing", "client", "problem", "solution", "retainer", "statement of work", "sow", "engagement", "budget", "milestone", "approval", "contract"],
    "market_research_report": ["market overview", "tam", "sam", "som", "competitor analysis", "swot", "go-to-market", "persona", "pricing landscape", "market sizing", "trends", "industry analysis", "benchmark", "segment", "demographics", "survey", "consumer insight", "market share", "growth rate", "forecast"],
    "executive_report": ["executive summary", "kpi", "dashboard", "quarterly", "annual report", "performance", "revenue", "operations", "board", "stakeholder", "roi", "strategic", "initiative", "roadmap"],
    "legal_brief": ["brief", "memorandum", "plaintiff", "defendant", "statute", "jurisdiction", "counsel", "court", "legal", "pleading", "motion", "contract", "compliance"],
    "incident_response_report": ["incident", "breach", "containment", "remediation", "eradication", "root cause", "forensics", "evidence", "affected systems", "timeline of events", "lessons learned", "ir report", "post-incident", "triage", "recovery"],
    "investment_memo": ["investment", "irr", "ebitda", "revenue", "valuation", "cap table", "term sheet", "due diligence", "portfolio", "returns", "fund", "lp", "gp", "deal", "thesis", "exit"],
    "narrative_nonfiction": ["true story", "memoir", "biography", "journalism", "reportage", "nonfiction", "non-fiction", "investigative", "chronicle"],
}


def detect_document_type(mode: str, title: str = "", genre: str = "", premise: str = "", writing_notes: str = "") -> str:
    if mode != "report":
        return MODE_TO_DEFAULT_DOC_TYPE.get(mode, "executive_report")
    haystack = " ".join([title, genre, premise, writing_notes]).lower()
    scores: Dict[str, int] = {dt: 0 for dt in DOC_TYPE_KEYWORDS}
    for doc_type, keywords in DOC_TYPE_KEYWORDS.items():
        for keyword in keywords:
            if keyword in haystack:
                scores[doc_type] += 1
    best = max(scores, key=lambda k: scores[k])
    if scores[best] > 0:
        return best
    return MODE_TO_DEFAULT_DOC_TYPE["report"]


def _prune_literary_blocks(profile: Dict[str, Any]) -> Dict[str, Any]:
    if profile.get("mode") in ("novel", "short_story", "poetry"):
        profile = dict(profile)
        profile["uses_tables"] = False
        profile["allowed_blocks"] = [b for b in profile.get("allowed_blocks", []) if b not in {"table", "chart", "risk_matrix", "swot_matrix", "comparison_matrix", "pie_chart", "bar_chart", "donut_chart", "line_chart", "kpi_cards"}]
    return profile


def get_document_profile(mode: str, document_type: str | None = None, *, title: str = "", genre: str = "", premise: str = "", writing_notes: str = "") -> Dict[str, Any]:
    if not document_type:
        document_type = detect_document_type(mode, title=title, genre=genre, premise=premise, writing_notes=writing_notes)
    if mode != "report":
        document_type = MODE_TO_DEFAULT_DOC_TYPE.get(mode, document_type)
    if document_type not in DOC_PROFILES:
        document_type = MODE_TO_DEFAULT_DOC_TYPE.get(mode, "executive_report")
    profile = dict(DOC_PROFILES[document_type])
    profile["document_type"] = document_type
    profile["mode"] = mode
    profile["allowed_blocks"] = list(profile.get("allowed_blocks", []))
    return _prune_literary_blocks(profile)
