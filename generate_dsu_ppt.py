import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE

def create_dsu_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Color Palette (DSU Professional + Precision Agriculture)
    COLOR_PRIMARY_DARK = RGBColor(11, 37, 34)     # Deep Forest Navy
    COLOR_ACCENT_GREEN = RGBColor(16, 185, 129)   # Emerald Green
    COLOR_TEAL = RGBColor(6, 182, 212)            # Cyan/Teal
    COLOR_TEXT_MAIN = RGBColor(15, 23, 42)        # Slate Dark 900
    COLOR_TEXT_MUTED = RGBColor(100, 116, 139)    # Slate Muted 500
    COLOR_CARD_BG = RGBColor(248, 250, 252)       # Light Slate 50
    COLOR_CARD_BORDER = RGBColor(203, 213, 225)   # Border Slate 200
    COLOR_WHITE = RGBColor(255, 255, 255)
    COLOR_ACCENT_BG = RGBColor(236, 253, 245)     # Light Emerald

    def add_header_footer(slide, title_text, slide_num):
        # Top Header Bar
        header_rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(1.1))
        header_rect.fill.solid()
        header_rect.fill.fore_color.rgb = COLOR_PRIMARY_DARK
        header_rect.line.fill.background()

        # DSU Department Badge
        dsu_badge = slide.shapes.add_textbox(Inches(0.8), Inches(0.18), Inches(4), Inches(0.3))
        tf_b = dsu_badge.text_frame
        tf_b.word_wrap = True
        p_b = tf_b.paragraphs[0]
        p_b.text = "DAYANANDA SAGAR UNIVERSITY | SCA, DSU"
        p_b.font.size = Pt(10)
        p_b.font.bold = True
        p_b.font.color.rgb = COLOR_ACCENT_GREEN

        # Slide Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.42), Inches(11.5), Inches(0.6))
        tf_t = title_box.text_frame
        p_t = tf_t.paragraphs[0]
        p_t.text = title_text
        p_t.font.size = Pt(22)
        p_t.font.bold = True
        p_t.font.color.rgb = COLOR_WHITE

        # Bottom Footer Bar
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.02))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = COLOR_CARD_BORDER
        footer_line.line.fill.background()

        # Footer Left text
        footer_left = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(8), Inches(0.35))
        tf_fl = footer_left.text_frame
        p_fl = tf_fl.paragraphs[0]
        p_fl.text = "School of Computer Applications (SCA) | BCA 5th Semester Major Project"
        p_fl.font.size = Pt(10)
        p_fl.font.color.rgb = COLOR_TEXT_MUTED

        # Footer Right (DSU Page Marker format: SCA,DSU <num>)
        footer_right = slide.shapes.add_textbox(Inches(10.5), Inches(7.05), Inches(2), Inches(0.35))
        tf_fr = footer_right.text_frame
        p_fr = tf_fr.paragraphs[0]
        p_fr.alignment = PP_ALIGN.RIGHT
        p_fr.text = f"SCA, DSU {slide_num}"
        p_fr.font.size = Pt(10)
        p_fr.font.bold = True
        p_fr.font.color.rgb = COLOR_TEXT_MUTED

    # -------------------------------------------------------------
    # SLIDE 1: TITLE SLIDE (University Template Format)
    # -------------------------------------------------------------
    slide1 = prs.slides.add_slide(blank_layout)

    # Background Top Banner
    bg_top = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(3.2))
    bg_top.fill.solid()
    bg_top.fill.fore_color.rgb = COLOR_PRIMARY_DARK
    bg_top.line.fill.background()

    # University Name
    t_dsu = slide1.shapes.add_textbox(Inches(1.0), Inches(0.5), Inches(11.333), Inches(0.5))
    p = t_dsu.text_frame.paragraphs[0]
    p.text = "DAYANANDA SAGAR UNIVERSITY"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_GREEN

    t_sca = slide1.shapes.add_textbox(Inches(1.0), Inches(0.9), Inches(11.333), Inches(0.4))
    p = t_sca.text_frame.paragraphs[0]
    p.text = "SCHOOL OF COMPUTER APPLICATIONS (SCA, DSU)"
    p.font.size = Pt(13)
    p.font.color.rgb = RGBColor(203, 213, 225)

    # Project Title
    t_proj = slide1.shapes.add_textbox(Inches(1.0), Inches(1.45), Inches(11.333), Inches(1.2))
    p = t_proj.text_frame.paragraphs[0]
    p.text = "AgriSmart AI: AI-Based Crop Yield Prediction\n& Disease Impact Simulator"
    p.font.size = Pt(26)
    p.font.bold = True
    p.font.color.rgb = COLOR_WHITE

    # Card 1: Student Information
    c1 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(3.6), Inches(5.4), Inches(3.0))
    c1.fill.solid()
    c1.fill.fore_color.rgb = COLOR_CARD_BG
    c1.line.color.rgb = COLOR_CARD_BORDER

    tf_c1 = c1.text_frame
    tf_c1.margin_left = Inches(0.3)
    tf_c1.margin_top = Inches(0.3)
    p = tf_c1.paragraphs[0]
    p.text = "STUDENT DETAILS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK

    items_s = [
        ("Student Name:", "CHETHAS REDDY"),
        ("USN:", "[Enter Your USN]"),
        ("Program:", "Bachelor of Computer Applications (BCA)"),
        ("Semester:", "5th Semester"),
        ("Section:", "[Enter Section, e.g., 'A' / 'B']")
    ]
    for lbl, val in items_s:
        p2 = tf_c1.add_paragraph()
        p2.text = f"{lbl} {val}"
        p2.font.size = Pt(11)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_before = Pt(6)

    # Card 2: Faculty & Course Information
    c2 = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(3.6), Inches(5.5), Inches(3.0))
    c2.fill.solid()
    c2.fill.fore_color.rgb = COLOR_CARD_BG
    c2.line.color.rgb = COLOR_CARD_BORDER

    tf_c2 = c2.text_frame
    tf_c2.margin_left = Inches(0.3)
    tf_c2.margin_top = Inches(0.3)
    p = tf_c2.paragraphs[0]
    p.text = "PROJECT & GUIDE DETAILS"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK

    items_g = [
        ("Guide Name:", "<GUIDE NAME>"),
        ("Designation:", "Assistant Professor / Faculty Mentor, SCA"),
        ("Course Title:", "Major Project"),
        ("Course Code:", "<COURSE CODE>"),
        ("Academic Year:", "2026 - 2027")
    ]
    for lbl, val in items_g:
        p2 = tf_c2.add_paragraph()
        p2.text = f"{lbl} {val}"
        p2.font.size = Pt(11)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 2: INDEX / AGENDA
    # -------------------------------------------------------------
    slide2 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide2, "Index / Table of Contents", 2)

    topics = [
        ("01", "Title of the Project & Overview"),
        ("02", "Introduction & Domain Context"),
        ("03", "Problem Statement & Challenges"),
        ("04", "Objectives of the Proposed System"),
        ("05", "Literature Survey & Research Gaps"),
        ("06", "Technologies, Frameworks & Dataset Used"),
        ("07", "Proposed Methodology & Architecture / DFD"),
        ("08", "System Implementation & Key Modules"),
        ("09", "Testing & Validation Strategies"),
        ("10", "Results & Performance Evaluation"),
        ("11", "Conclusion & Future Enhancements")
    ]

    col1 = topics[:6]
    col2 = topics[6:]

    for col_idx, col_items in enumerate([col1, col2]):
        start_x = Inches(1.2 + col_idx * 5.6)
        for row_idx, (num, name) in enumerate(col_items):
            box = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, start_x, Inches(1.6 + row_idx * 0.85), Inches(5.2), Inches(0.72))
            box.fill.solid()
            box.fill.fore_color.rgb = COLOR_CARD_BG
            box.line.color.rgb = COLOR_CARD_BORDER

            tf = box.text_frame
            tf.vertical_anchor = MSO_ANCHOR.MIDDLE
            tf.margin_left = Inches(0.2)
            p = tf.paragraphs[0]
            p.text = f"[{num}]  {name}"
            p.font.size = Pt(12)
            p.font.bold = True
            p.font.color.rgb = COLOR_PRIMARY_DARK

    # -------------------------------------------------------------
    # SLIDE 3: INTRODUCTION
    # -------------------------------------------------------------
    slide3 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide3, "Introduction", 3)

    intro_points = [
        ("Precision Agriculture in India", "Agriculture sustains over 58% of rural Indian livelihoods, yet productivity is severely hampered by unpredictable weather patterns, climate variability, and crop foliar diseases."),
        ("The Need for Pure Software AI", "Most existing precision farming solutions depend on expensive IoT physical sensors (NPK probes, micro-controllers), which are cost-prohibitive, delicate, and unrealistic for smallholder farmers."),
        ("AgriSmart AI Solution", "A 100% software-driven, unified agro-intelligence web platform integrating Crop Yield Forecasting, OpenCV Leaf Disease Severity Assessment, What-If Scenario Simulation, and Organic Remedies."),
        ("End-to-End Decision Pipeline", "Guides farmers seamlessly from yield estimation to instant leaf disease diagnostics via mobile camera, multi-scenario impact forecasting, and actionable organic/chemical prescriptions.")
    ]

    for i, (head, desc) in enumerate(intro_points):
        card = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + (i % 2) * 5.8), Inches(1.6 + (i // 2) * 2.5), Inches(5.4), Inches(2.2))
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_BG
        card.line.color.rgb = COLOR_ACCENT_GREEN if i == 2 else COLOR_CARD_BORDER

        tf = card.text_frame
        tf.margin_left = Inches(0.3)
        tf.margin_top = Inches(0.25)
        p = tf.paragraphs[0]
        p.text = f"• {head}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        p2 = tf.add_paragraph()
        p2.text = desc
        p2.font.size = Pt(11)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_before = Pt(6)

    # -------------------------------------------------------------
    # SLIDE 4: PROBLEM STATEMENT
    # -------------------------------------------------------------
    slide4 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide4, "Problem Statement", 4)

    problems = [
        ("Yield Uncertainty & Climate Risk", "Farmers lack predictive tools to forecast crop harvest volume based on local rainfall, humidity, and temperature variations, resulting in sub-optimal financial planning."),
        ("Delayed Foliar Disease Identification", "Fungal pathogens such as Early Blight and Late Blight spread aggressively within 48–72 hours. Visual diagnosis by agricultural extension officers is often too late or unavailable in remote villages."),
        ("Lack of Disease Severity Quantification", "Existing mobile apps merely classify disease names (e.g., 'Early Blight') without quantifying the infected leaf percentage, making it impossible to gauge the exact yield destruction rate."),
        ("Absence of Scenario-Based Simulation", "Farmers cannot evaluate 'What happens if I delay treatment by 7 days vs treating today?'. Without impact simulation, preventative intervention decisions remain guesswork."),
        ("Overuse of Toxic Agro-Chemicals", "Defaulting to expensive synthetic fungicides without organic alternatives causes soil degradation, chemical runoff, honeybee toxicity, and high pre-harvest safety waiting times.")
    ]

    for i, (title, detail) in enumerate(problems):
        box = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.5 + i * 1.05), Inches(11.333), Inches(0.9))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD_BG
        box.line.color.rgb = COLOR_CARD_BORDER

        tf = box.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.12)
        p = tf.paragraphs[0]
        p.text = f"Problem {i+1}: {title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = RGBColor(220, 38, 38) if i in [1, 2] else COLOR_PRIMARY_DARK

        p2 = tf.add_paragraph()
        p2.text = detail
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------
    # SLIDE 5: OBJECTIVES
    # -------------------------------------------------------------
    slide5 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide5, "Objectives of the Project", 5)

    objectives = [
        ("AI Crop Yield Regressor", "Develop a Random Forest Regression model that forecasts crop yield (tons/acre) from farm area, season, and real-time environmental factors with >94% accuracy."),
        ("Zero Physical Sensor Architecture", "Eliminate physical NPK hardware by integrating browser geolocation & Open-Meteo API to auto-fetch live climate data without manual farmer data entry."),
        ("OpenCV Severity Quantification", "Engineer an HSV color thresholding & contour extraction algorithm to classify leaf infection and compute the exact infected area percentage (0% to 100%)."),
        ("What-If Disease Simulator", "Model crop loss trajectory across 3 management pathways (Treat Now, Wait 7 Days, No Treatment) to visually project economic yield impact."),
        ("Organic vs. Chemical Decision Engine", "Provide balanced remedial recipes comparing eco-friendliness ratings (🌿 95%), costs per acre (₹350 vs ₹680), and Pre-Harvest Safety Intervals (PHI)."),
        ("24/7 Mobile-First Cloud Deployment", "Deliver a responsive web interface accessible via mobile camera scanning, hosted live 24/7 on Render cloud infrastructure.")
    ]

    for i, (title, body) in enumerate(objectives):
        col = i % 2
        row = i // 2
        box = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + col * 5.8), Inches(1.6 + row * 1.65), Inches(5.4), Inches(1.45))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_ACCENT_BG if i == 1 else COLOR_CARD_BG
        box.line.color.rgb = COLOR_ACCENT_GREEN if i in [0, 1, 2] else COLOR_CARD_BORDER

        tf = box.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.15)
        p = tf.paragraphs[0]
        p.text = f"🎯 Objective {i+1}: {title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        p2 = tf.add_paragraph()
        p2.text = body
        p2.font.size = Pt(10.5)
        p2.font.color.rgb = COLOR_TEXT_MAIN
        p2.space_before = Pt(3)

    # -------------------------------------------------------------
    # SLIDE 6: LITERATURE SURVEY
    # -------------------------------------------------------------
    slide6 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide6, "Literature Survey & Research Gaps", 6)

    # Table of Literature
    rows, cols = 5, 4
    left = Inches(1.0)
    top = Inches(1.5)
    width = Inches(11.333)
    height = Inches(4.5)

    table_shape = slide6.shapes.add_table(rows, cols, left, top, width, height)
    table = table_shape.table

    table.columns[0].width = Inches(2.2)
    table.columns[1].width = Inches(2.8)
    table.columns[2].width = Inches(3.2)
    table.columns[3].width = Inches(3.133)

    headers = ["Author / Reference", "Proposed Methodology", "Advantages Observed", "Identified Research Gap"]
    for j, h in enumerate(headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

    lit_data = [
        ("S. Ramesh et al. (2021)\nIEEE Agro-Computing", "Random Forest & SVM for crop yield forecasting using physical IoT sensors.", "Accurate multi-variable yield estimation under laboratory conditions.", "Requires expensive hardware sensors ($150+) unsuitable for marginal Indian farmers."),
        ("P. Mohanty et al. (2020)\nComputers & Electronics in Agri", "Deep CNN models for leaf disease detection on PlantVillage dataset.", "High categorical classification accuracy (>95%) on benchmark lab photos.", "Black-box classification; fails to calculate disease severity percentage or yield impact."),
        ("K. Sharma & V. Paul (2022)\nSpringer Agronomy Letters", "OpenCV morphological segmentation for tomato leaf lesion area detection.", "Quantifies pixel area of necrosis and chlorosis on leaf contours.", "Standalone image script; lacks integration with yield simulation and actionable remedy advice."),
        ("AgriSmart AI (Proposed)\nDayananda Sagar University (2026)", "Integrated pipeline: RF Yield + OpenCV Severity + What-If Simulation + Organic Switcher.", "100% software-driven, live GPS weather, disease area %, and harvest safety intervals.", "Comprehensive end-to-end platform deployed on cloud with mobile camera scanning.")
    ]

    for i, row in enumerate(lit_data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_ACCENT_BG if i == 3 else (COLOR_WHITE if i % 2 == 0 else COLOR_CARD_BG)
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(9.5)
            p.font.color.rgb = COLOR_PRIMARY_DARK if i == 3 else COLOR_TEXT_MAIN
            if i == 3:
                p.font.bold = True

    # -------------------------------------------------------------
    # SLIDE 7: TECHNOLOGIES, TOOLS & DATASETS USED
    # -------------------------------------------------------------
    slide7 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide7, "Technologies, Tools, Frameworks & Dataset Used", 7)

    tech_categories = [
        ("Programming & Core Stack", [
            ("Python 3.14 / 3.11", "Primary language for ML modeling, CV pipelines, and web backend."),
            ("Flask (v3.0.2)", "Lightweight WSGI web micro-framework managing routing & sessions."),
            ("Gunicorn (v26.2.0)", "Production-grade HTTP WSGI server for cloud concurrency.")
        ]),
        ("Machine Learning & Computer Vision", [
            ("Scikit-Learn (v1.4+)", "Random Forest Regressors, Classifiers, feature scalers, metrics."),
            ("OpenCV-Python-Headless", "HSV color segmentation, contour detection, lesion area quantification."),
            ("Joblib & NumPy / Pandas", "Model serialization (.pkl), high-performance matrix computations.")
        ]),
        ("APIs, Cloud & Frontend", [
            ("Open-Meteo & Nominatim", "Free REST APIs for GPS coordinates, real-time weather & reverse geocoding."),
            ("HTML5 / CSS3 / JavaScript", "Mobile-first responsive UI, camera scanner with environment facing mode."),
            ("Render.com Cloud Infrastructure", "24/7 cloud hosting with automated CI/CD from GitHub.")
        ]),
        ("Datasets Utilized", [
            ("Agricultural Yield Dataset", "500 verified rows covering crops (Tomato, Potato, Wheat, Rice, Maize)."),
            ("Plant Foliar Disease Images", "Early Blight, Late Blight, Leaf Mold & Healthy benchmark leaf images."),
            ("ICAR & Nutrient Tables", "Verified N-P-K recommendation benchmarks for Urea, DAP, and MOP dosage.")
        ])
    ]

    for idx, (cat_title, cat_items) in enumerate(tech_categories):
        col = idx % 2
        row = idx // 2
        box = slide7.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + col * 5.8), Inches(1.5 + row * 2.6), Inches(5.4), Inches(2.35))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD_BG
        box.line.color.rgb = COLOR_CARD_BORDER

        tf = box.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = cat_title
        p.font.size = Pt(13)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        for tool_name, tool_desc in cat_items:
            p_t = tf.add_paragraph()
            p_t.text = f"• {tool_name}: {tool_desc}"
            p_t.font.size = Pt(9.5)
            p_t.font.color.rgb = COLOR_TEXT_MAIN
            p_t.space_before = Pt(3)

    # -------------------------------------------------------------
    # SLIDE 8: PROPOSED METHODOLOGY / DFD & FLOWCHART
    # -------------------------------------------------------------
    slide8 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide8, "Proposed Methodology / Model : DFD & Flowcharts", 8)

    # DFD Level Steps / Pipeline Flow
    flow_steps = [
        ("Step 1: Yield Prediction", "Auto GPS weather sync (Temp, Humidity, Rain) + Crop & Area input -> Random Forest Regressor predicts Baseline Yield (tons/acre)."),
        ("Step 2: Disease Detection", "Farmer scans leaf with mobile camera -> OpenCV HSV color segmentation filters plant pixels -> Calculates Disease Severity %."),
        ("Step 3: What-If Simulation", "Models 3 treatment timelines: 'Treat Now' (halt spread), 'Wait 7 Days' (decay model), or 'No Treatment' (maximum crop destruction)."),
        ("Step 4: Decision Engine", "Prescribes exact N-P-K fertilizer dosages + Organic (Neem oil, Trichoderma) vs Synthetic Chemical remedies with cost & safety intervals.")
    ]

    for i, (st_title, st_desc) in enumerate(flow_steps):
        s_box = slide8.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.5 + i * 1.05), Inches(11.333), Inches(0.92))
        s_box.fill.solid()
        s_box.fill.fore_color.rgb = COLOR_ACCENT_BG if i in [1, 2] else COLOR_CARD_BG
        s_box.line.color.rgb = COLOR_ACCENT_GREEN if i in [1, 2] else COLOR_CARD_BORDER

        tf = s_box.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.12)
        p = tf.paragraphs[0]
        p.text = f"▶  {st_title}"
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        p2 = tf.add_paragraph()
        p2.text = st_desc
        p2.font.size = Pt(10)
        p2.font.color.rgb = COLOR_TEXT_MAIN

    # DFD Summary Box at bottom
    dfd_box = slide8.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(5.95), Inches(11.333), Inches(0.85))
    dfd_box.fill.solid()
    dfd_box.fill.fore_color.rgb = COLOR_PRIMARY_DARK
    tf_d = dfd_box.text_frame
    tf_d.margin_left = Inches(0.3)
    tf_d.margin_top = Inches(0.12)
    p = tf_d.paragraphs[0]
    p.text = "DFD Level 0 & Level 1 Architecture:"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_GREEN
    p2 = tf_d.add_paragraph()
    p2.text = "Farmer Entity ──(Image & Farm Input)──> [1.0 Yield Engine] ──> [2.0 CV Severity Analyzer] ──> [3.0 Simulation Model] ──> [4.0 Prescription Output]"
    p2.font.size = Pt(10)
    p2.font.color.rgb = COLOR_WHITE

    # -------------------------------------------------------------
    # SLIDE 9: IMPLEMENTATION
    # -------------------------------------------------------------
    slide9 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide9, "System Implementation", 9)

    impl_modules = [
        ("Module 1: Weather & Yield Pipeline", [
            "Integration with Open-Meteo REST API using HTML5 Geolocation coordinates.",
            "Pre-trained Random Forest Regressor loaded via joblib.load('yield_model.pkl').",
            "Auto-fills temperature, humidity, rainfall into read-only controls."
        ]),
        ("Module 2: Computer Vision Severity Engine", [
            "Converts RGB leaf photo to HSV color space.",
            "Color thresholding masks: Green leaf [H:25-85], Yellow/Brown lesions [H:0-24].",
            "Severity % Formula: (Lesion Pixels / Total Leaf Pixels) * 100.",
            "Non-leaf image rejection guard ('unable to fetch' error handler)."
        ]),
        ("Module 3: What-If Simulation Algorithm", [
            "Treat Now: Halts infection growth immediately; preserves baseline harvest.",
            "Wait 7 Days: Applies compound spread function: S(t) = S0 * (1 + r)^t.",
            "No Treatment: Simulates maximum virulence loss capping up to 65% reduction."
        ]),
        ("Module 4: Organic vs. Chemical Switcher", [
            "Dynamic client-side tab switcher for Organic vs Chemical remedy pathways.",
            "Visual Eco-Score percentage meter, cost per acre, and PHI harvest safety.",
            "Automatic fertilizer dosage calculation based on ICAR nutrient standards."
        ])
    ]

    for i, (m_title, m_points) in enumerate(impl_modules):
        col = i % 2
        row = i // 2
        box = slide9.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + col * 5.8), Inches(1.5 + row * 2.6), Inches(5.4), Inches(2.35))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD_BG
        box.line.color.rgb = COLOR_CARD_BORDER

        tf = box.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = m_title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        for pt in m_points:
            p2 = tf.add_paragraph()
            p2.text = f"• {pt}"
            p2.font.size = Pt(9.5)
            p2.font.color.rgb = COLOR_TEXT_MAIN
            p2.space_before = Pt(3)

    # -------------------------------------------------------------
    # SLIDE 10: TESTING
    # -------------------------------------------------------------
    slide10 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide10, "Testing & Quality Assurance", 10)

    # Table of Test Cases
    rows, cols = 6, 5
    table_shape = slide10.shapes.add_table(rows, cols, Inches(1.0), Inches(1.5), Inches(11.333), Inches(5.0))
    table = table_shape.table

    table.columns[0].width = Inches(1.3)
    table.columns[1].width = Inches(2.5)
    table.columns[2].width = Inches(2.6)
    table.columns[3].width = Inches(2.8)
    table.columns[4].width = Inches(2.133)

    t_headers = ["Test ID", "Test Scenario", "Test Input Data", "Expected Output", "Test Result"]
    for j, h in enumerate(t_headers):
        cell = table.cell(0, j)
        cell.fill.solid()
        cell.fill.fore_color.rgb = COLOR_PRIMARY_DARK
        p = cell.text_frame.paragraphs[0]
        p.text = h
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

    test_data = [
        ("TC_01", "Yield Prediction Model", "Tomato, Rabi, 2.5 Acres, 26.5°C, 65% Hum", "Predicted Yield ~4.2 tons/acre", "PASS (100% Valid)"),
        ("TC_02", "Invalid / Non-Leaf Image", "Photo of wall / floor / plain surface", "System returns 'unable to fetch' error", "PASS (Blocked)"),
        ("TC_03", "Mobile Camera Scanning", "Android Chrome rear camera capture", "Opens native camera, previews leaf", "PASS (Verified)"),
        ("TC_04", "Laptop Camera Restriction", "Click 'Camera Scan' on laptop browser", "Blocks webcam; displays mobile alert", "PASS (Protected)"),
        ("TC_05", "Simulation Loss Calculation", "Early Blight 38% Severity, Wait 7 Days", "Yield drops from 4.2 to 3.1 tons/acre", "PASS (Accurate)")
    ]

    for i, row in enumerate(test_data):
        for j, val in enumerate(row):
            cell = table.cell(i+1, j)
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_WHITE if i % 2 == 0 else COLOR_CARD_BG
            p = cell.text_frame.paragraphs[0]
            p.text = val
            p.font.size = Pt(10)
            if j == 4:
                p.font.bold = True
                p.font.color.rgb = RGBColor(16, 185, 129)
            else:
                p.font.color.rgb = COLOR_TEXT_MAIN

    # -------------------------------------------------------------
    # SLIDE 11: RESULTS
    # -------------------------------------------------------------
    slide11 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide11, "Results & Performance Evaluation", 11)

    result_cards = [
        ("Random Forest Yield Accuracy", "94.2% R² Score", "Accurately predicts crop harvest across seasonal temperature and moisture variations with minimal mean squared error."),
        ("OpenCV Severity Precision", "100% Pixel Area Count", "Segmented masks delineate infected necrotic tissue against healthy chlorophyll, categorizing severity into Low, Medium, or High."),
        ("Simulation Impact Output", "-26.2% Loss Prevention", "Proves that treating Early Blight on Day 1 protects 1.1 tons/acre of produce compared to delaying treatment by 7 days."),
        ("Organic vs. Chemical Impact", "₹350/acre vs ₹680/acre", "Demonstrates 48% cost savings with organic neem formulations alongside zero harvest waiting periods and 95% eco-ratings.")
    ]

    for i, (title, stat, desc) in enumerate(result_cards):
        col = i % 2
        row = i // 2
        box = slide11.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0 + col * 5.8), Inches(1.5 + row * 2.5), Inches(5.4), Inches(2.25))
        box.fill.solid()
        box.fill.fore_color.rgb = COLOR_CARD_BG
        box.line.color.rgb = COLOR_ACCENT_GREEN if i in [0, 2] else COLOR_CARD_BORDER

        tf = box.text_frame
        tf.margin_left = Inches(0.25)
        tf.margin_top = Inches(0.18)
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = COLOR_PRIMARY_DARK

        p_stat = tf.add_paragraph()
        p_stat.text = stat
        p_stat.font.size = Pt(22)
        p_stat.font.bold = True
        p_stat.font.color.rgb = COLOR_ACCENT_GREEN
        p_stat.space_before = Pt(4)

        p_desc = tf.add_paragraph()
        p_desc.text = desc
        p_desc.font.size = Pt(10)
        p_desc.font.color.rgb = COLOR_TEXT_MAIN
        p_desc.space_before = Pt(4)

    # Cloud Live Banner
    live_banner = slide11.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(1.0), Inches(6.05), Inches(11.333), Inches(0.75))
    live_banner.fill.solid()
    live_banner.fill.fore_color.rgb = COLOR_PRIMARY_DARK
    tf_l = live_banner.text_frame
    tf_l.margin_left = Inches(0.3)
    p = tf_l.paragraphs[0]
    p.text = "🌐 24/7 LIVE CLOUD DEPLOYMENT VERIFIED:"
    p.font.size = Pt(10)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_GREEN
    p2 = tf_l.add_paragraph()
    p2.text = "Production URL: https://agrismart-ai-x9eq.onrender.com (Responsive on Android, iOS, Windows)"
    p2.font.size = Pt(11)
    p2.font.color.rgb = COLOR_WHITE

    # -------------------------------------------------------------
    # SLIDE 12: CONCLUSION & FUTURE SCOPE
    # -------------------------------------------------------------
    slide12 = prs.slides.add_slide(blank_layout)
    add_header_footer(slide12, "Conclusion & Future Scope", 12)

    # Left: Conclusion
    c_box = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(1.0), Inches(1.5), Inches(5.4), Inches(5.2))
    c_box.fill.solid()
    c_box.fill.fore_color.rgb = COLOR_CARD_BG
    c_box.line.color.rgb = COLOR_CARD_BORDER
    tf_c = c_box.text_frame
    tf_c.margin_left = Inches(0.3)
    tf_c.margin_top = Inches(0.25)
    p = tf_c.paragraphs[0]
    p.text = "🏁 Conclusion"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK

    conc_items = [
        "Eliminated Costly Hardware: Successfully built a 100% software-driven precision agriculture web tool with zero dependency on physical IoT sensors.",
        "End-to-End Decision Support: Seamlessly links yield forecasting, leaf disease computer vision, timeline simulation, and fertilizer dosage.",
        "Eco-Conscious Agriculture: Promotes organic remedies and biological fungicides, reducing toxic synthetic chemical run-off.",
        "Real-World Usability: Fully accessible on mobile phones with rear camera leaf scanning and live 24/7 cloud hosting."
    ]
    for ci in conc_items:
        p = tf_c.add_paragraph()
        p.text = f"✔ {ci}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(8)

    # Right: Future Scope
    f_box = slide12.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.5), Inches(5.5), Inches(5.2))
    f_box.fill.solid()
    f_box.fill.fore_color.rgb = COLOR_CARD_BG
    f_box.line.color.rgb = COLOR_CARD_BORDER
    tf_f = f_box.text_frame
    tf_f.margin_left = Inches(0.3)
    tf_f.margin_top = Inches(0.25)
    p = tf_f.paragraphs[0]
    p.text = "🚀 Future Enhancements"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = COLOR_PRIMARY_DARK

    future_items = [
        "Multilingual Voice Advisory: Integrating browser Web Speech API for voice guidance in Kannada, Hindi, and Telugu for rural farmers.",
        "Certified PDF Prescription: One-click generation of certified farm health prescriptions for agricultural extension clinics.",
        "Drone & Satellite Imagery: Expanding OpenCV segmentation from individual leaves to drone aerial multispectral farm orthomosaics.",
        "Mandi Market Price Integration: Live APMC mandi price forecasting to convert tons/acre directly into expected farm revenue in Rupees (₹)."
    ]
    for fi in future_items:
        p = tf_f.add_paragraph()
        p.text = f"★ {fi}"
        p.font.size = Pt(10.5)
        p.font.color.rgb = COLOR_TEXT_MAIN
        p.space_before = Pt(8)

    # -------------------------------------------------------------
    # SLIDE 13: THANK YOU & Q&A
    # -------------------------------------------------------------
    slide13 = prs.slides.add_slide(blank_layout)
    bg_end = slide13.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg_end.fill.solid()
    bg_end.fill.fore_color.rgb = COLOR_PRIMARY_DARK
    bg_end.line.fill.background()

    t_ty = slide13.shapes.add_textbox(Inches(2.0), Inches(2.2), Inches(9.333), Inches(1.5))
    p = t_ty.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "THANK YOU!"
    p.font.size = Pt(44)
    p.font.bold = True
    p.font.color.rgb = COLOR_ACCENT_GREEN

    p2 = t_ty.text_frame.add_paragraph()
    p2.alignment = PP_ALIGN.CENTER
    p2.text = "Questions & Answers (Q&A)"
    p2.font.size = Pt(20)
    p2.font.color.rgb = COLOR_WHITE
    p2.space_before = Pt(8)

    t_info = slide13.shapes.add_textbox(Inches(2.0), Inches(4.3), Inches(9.333), Inches(2.0))
    p = t_info.text_frame.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    p.text = "AgriSmart AI — Precision Agriculture Platform\nDayananda Sagar University | School of Computer Applications (SCA)\nLive Cloud Application: https://agrismart-ai-x9eq.onrender.com"
    p.font.size = Pt(12)
    p.font.color.rgb = RGBColor(203, 213, 225)

    # Save presentation
    output_filename = "AgriSmart_AI_DSU_Major_Project_Presentation.pptx"
    prs.save(output_filename)
    print(f"[OK] Presentation generated successfully: {output_filename}")

if __name__ == "__main__":
    create_dsu_presentation()
