import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# Initialize PowerPoint Presentation
prs = Presentation()

# Set slide size to modern Widescreen (16:9 aspect ratio)
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)

# Style Design Palette (Slate Navy & Emerald Teal)
COLOR_NAVY = RGBColor(15, 23, 42)      # Main Titles & Branding (#0f172a)
COLOR_TEAL = RGBColor(13, 148, 136)   # Accents & Highlights (#0d9488)
COLOR_TEXT = RGBColor(51, 65, 85)     # Readable Charcoal Body Text (#334155)
COLOR_LIGHT_BG = RGBColor(241, 245, 249) # Light container backgrounds (#f1f5f9)
FONT_NAME = "Calibri"

blank_layout = prs.slide_layouts[6] # Fully blank layout for absolute design control

def create_title_slide(prs, title, subtitle, presenter, dept, supervisor):
    """Generates a custom designed, professional title slide"""
    slide = prs.slides.add_slide(blank_layout)
    
    # Left accent colored panel
    left_panel = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0), Inches(0), Inches(0.4), Inches(7.5))
    left_panel.fill.solid()
    left_panel.fill.fore_color.rgb = COLOR_TEAL
    left_panel.line.fill.background()
    
    # Title Text Box
    title_box = slide.shapes.add_textbox(Inches(1.0), Inches(1.5), Inches(11.333), Inches(2.2))
    tf = title_box.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = title
    p.font.name = FONT_NAME
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY
    
    # Subtitle Text Box
    sub_box = slide.shapes.add_textbox(Inches(1.0), Inches(3.8), Inches(11.333), Inches(1.0))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_sub = tf_sub.paragraphs[0]
    p_sub.text = subtitle
    p_sub.font.name = FONT_NAME
    p_sub.font.size = Pt(18)
    p_sub.font.italic = True
    p_sub.font.color.rgb = COLOR_TEAL
    
    # Metadata Box (Presenter, Dept, Supervisor)
    meta_box = slide.shapes.add_textbox(Inches(1.0), Inches(5.0), Inches(11.333), Inches(1.8))
    tf_meta = meta_box.text_frame
    
    # Presenter Line
    p1 = tf_meta.paragraphs[0]
    p1.text = f"Presenter: {presenter}"
    p1.font.name = FONT_NAME
    p1.font.size = Pt(14)
    p1.font.bold = True
    p1.font.color.rgb = COLOR_TEXT
    
    # Dept Line
    p2 = tf_meta.add_paragraph()
    p2.text = f"Department: {dept}"
    p2.font.name = FONT_NAME
    p2.font.size = Pt(13)
    p2.font.color.rgb = COLOR_TEXT
    
    # Supervisor Line
    p3 = tf_meta.add_paragraph()
    p3.text = f"Supervisor Panel: {supervisor}"
    p3.font.name = FONT_NAME
    p3.font.size = Pt(13)
    p3.font.color.rgb = COLOR_TEXT

    return slide

def add_header(slide, title_text):
    """Adds a unified header with brand line to content slides"""
    # Header Text
    header_box = slide.shapes.add_textbox(Inches(0.75), Inches(0.4), Inches(11.833), Inches(1.0))
    tf = header_box.text_frame
    p = tf.paragraphs[0]
    p.text = title_text
    p.font.name = FONT_NAME
    p.font.size = Pt(28)
    p.font.bold = True
    p.font.color.rgb = COLOR_NAVY
    
    # Accent Underline
    line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), Inches(1.15), Inches(1.5), Inches(0.06))
    line.fill.solid()
    line.fill.fore_color.rgb = COLOR_TEAL
    line.line.fill.background()

slide_configs = [
    {
        "title": "Introduction & Research Background",
        "notes": "Good morning, members of the panel. I will begin by introducing the background. Paper attendance rosters invite massive proxy fraud and tracking overhead. While cloud-dependent systems solve this, they introduce critical issues like subscription overheads, severe bandwidth consumption, and total vulnerability to network dropouts. Shifting deep learning directly to local edge devices solves this, enabling offline runtime tracking.",
        "content_type": "bullets",
        "bullets": [
            "Traditional System Failure: Paper records facilitate proxy fraud and create tracking bottlenecks.",
            "Cloud-Dependency Risks: High bandwidth usage, subscription costs, and immediate failure on internet dropout.",
            "The Solution (Edge-AI): Shifting neural network analysis from cloud servers down to local user hardware.",
            "Core Technologies Combined: OpenCV (Video Capture), InsightFace (Embeddings), and Dynamic EAR (Liveness)."
        ]
    },
    {
        "title": "Statement of the Problem",
        "notes": "Our study addresses three distinct problems. First, 2D face scans are vulnerable to presentation attacks where photos easily bypass registration. Second, unoptimized neural models exhaust edge CPUs, dropping frame rates to unworkable levels. Third, static thresholds cause 'user exclusion' by failing on naturally diverse human eye phenotypes. We resolve these limitations structurally.",
        "content_type": "grid",
        "grid_items": [
            ("Biometric Spoofing", "Standard 2D face scanning lacks depth analysis and fails against basic printed photo presentation attacks."),
            ("CPU Starvation", "Heavy model zoos drain computer threads, triggering severe visual lag and system crashes on standard laptops."),
            ("Static Threshold Failures", "Fixed mathematical variables ignore natural human eye shapes, causing high false rejection counts.")
        ]
    },
    {
        "title": "Research Aim and Objectives",
        "notes": "The primary aim is to implement a secure, fully offline Edge-AI face recognition and liveness detection framework. We broke this down into four key steps: building an asynchronous vision pipeline, implementing an adaptive eye baseline tracking algorithm, establishing a deduplicated SQLite database structure, and compiling the code into a stable standalone windows application.",
        "content_type": "bullets",
        "bullets": [
            "Core Aim: To design, build, and deploy an offline, high-speed, secure Edge-AI attendance engine with dynamic liveness.",
            "Objective 1: Architect an Asynchronous Multithreaded execution pipeline to protect system responsiveness.",
            "Objective 2: Develop a dynamic Eye Aspect Ratio (EAR) baseline model for precise presentation attack deterrence.",
            "Objective 3: Establish a self-healing relational SQLite core integrating active biometric deduplication.",
            "Objective 4: Package the platform as a standalone Windows executable (.exe) fully optimized for edge deployment."
        ]
    },
    {
        "title": "System Architecture & Optimization",
        "notes": "To execute complex deep learning locally, we stripped unnecessary pipelines from the default InsightFace model zoo—bypassing 3D mapping and age/gender estimation. This saved massive CPU cycles. We then isolated tasks using multithreading: Thread 1 feeds the GUI loop seamlessly, while Thread 2 parses matrices in the background without freezing the window.",
        "content_type": "grid",
        "grid_items": [
            ("Module Restriction", "Deactivated 3D landmarking and age profiling from InsightFace to optimize local RAM and CPU thread usage."),
            ("Asynchronous Threads", "Decoupled code execution: Thread-1 maintains high UI frames while Thread-2 processes heavy background vector math."),
            ("Driver Direct Compiles", "Swapped buggy standard Windows media engines for native DirectShow drivers to eliminate memory leaks.")
        ]
    },
    {
        "title": "Core Mathematical Foundations",
        "notes": "The system relies on solid mathematical logic. For face recognition, we compute the Cosine Similarity to measure the angular displacement between vectors. For liveness detection, we capture localized coordinate clusters to find the Eye Aspect Ratio. Critically, our anti-spoofing maps blinks based on a strict 30% drop from that user's dynamic resting state.",
        "content_type": "math",
        "math_items": [
            ("Spatial Face Identification", "Cosine Similarity = (A \u22c5 B) / (||A|| ||B||)", "Calculates the exact angular vector displacement to identify users."),
            ("Liveness Coordinate Ratio", "EAR = v_dist / max(h_dist, 0.001)", "Maps 106-point eye tracking clusters to compute relative aspect ratios."),
            ("The Dynamic Blink Metric", "Blink Verification = 30% Drop from Dynamic Baseline", "Rejects photo prints and screens since they can't alter aspect ratios.")
        ]
    },
    {
        "title": "Face Recognition Performance Analysis",
        "notes": "To optimize verification, we tested the engine across 200 trials. Setting a loose threshold of 0.30 caused a high 15% False Acceptance Rate—this is unacceptable for attendance. Tightening to 0.60 blocked intruders but rejected 55% of legitimate students. By mapping our boundary to the 0.40–0.45 zone, we secured a perfect 0% FAR while keeping FRR below 5%.",
        "content_type": "table_recognition"
    },
    {
        "title": "Error Rate Trade-off Visualizer",
        "notes": "This slide points out Figure 4.2. As our similarity thresholds grow stricter, our False Acceptance Rate drops straight to zero, while False Rejection rises. The green highlighted zone shows our optimized operating zone between 0.40 and 0.45, where we completely block intruders while maintaining high user accessibility.",
        "content_type": "placeholder_image",
        "placeholder_text": "[ Insert Figure 4.2: Cosine Threshold Line Graph Here (Run generate_graph.py to get this image) ]"
    },
    {
        "title": "System Latency & Throughput Metrics",
        "notes": "This slide displays our computational efficiency. Running heavy networks sequentially on one thread blocks the GUI, resulting in a lagging 4.2 FPS. By shifting AI logic to background worker threads, the frame rate shot up to 32.5 FPS—a massive 7.7x performance acceleration on standard computer hardware without requiring expensive graphics cards.",
        "content_type": "table_latency"
    },
    {
        "title": "Throughput Evaluation Metrics",
        "notes": "This slide illustrates Figure 4.4, comparing baseline sequential operations against our multithreaded engine. The 7.7x execution boost allows the platform to run seamlessly on standard school computers, proving we don't need cloud hosting or specialized processing hardware to achieve responsive biometric security.",
        "content_type": "placeholder_image",
        "placeholder_text": "[ Insert Figure 4.4: FPS Comparison Bar Chart Here (Run generate_bar_chart.py to get this image) ]"
    },
    {
        "title": "Database Admin & Data Integrity Features",
        "notes": "Our platform includes complete administrative and database security tools. First, the database is self-healing, automatically rebuilding schemas on startup if compiled directories are moved. Second, we designed biometric deduplication, scanning face vectors during registration to block fraud. Third, cascade triggers ensure that deleting a student purges all corresponding logs.",
        "content_type": "grid",
        "grid_items": [
            ("Self-Healing Database", "The SQLite engine auto-constructs directories and structural tables if system paths are altered during packaging."),
            ("Active Deduplication", "Checks live face vectors against existing database buffers, blocking duplicate enrollment profiles."),
            ("Cascading Relational Wipes", "Enforces strict database referential integrity—dropping a student automatically drops all associated historical attendance logs.")
        ]
    },
    {
        "title": "Conclusion and Recommendations",
        "notes": "In conclusion, we have built a highly secure, offline, Edge-AI attendance tracking system that achieves 99% accuracy and 32.5 FPS. For future scaling, we recommend porting the decoupled logic into mobile Android apps, connecting triggers directly to physical examination hall turnstiles, and adding AES-256 block encryption over the raw facial templates. Thank you.",
        "content_type": "grid_dual",
        "col1_title": "Core Research Conclusions",
        "col1_bullets": [
            "Offline Edge-AI Success: Proved that secure, offline deep-learning models can run seamlessly on standard laptop CPUs.",
            "Dynamic Anti-Spoofing: Solved the 2D facial recognition photo bypass loop utilizing customized eye aspect ratio tracking.",
            "Optimized Frame Rates: Achieved a responsive 32.5 FPS, protecting GUI stability from high-intensity math bottlenecks."
        ],
        "col2_title": "Future Project Recommendations",
        "col2_bullets": [
            "Android Integration: Port the backend logic into lightweight, offline mobile frameworks for mobile convenience.",
            "Physical Entry Control: Connect system databases to physical microcontrollers to control examination hall gates.",
            "Template Protection: Wrap stored 512-dimensional facial embedding arrays inside secure AES-256 blocks."
        ]
    }
]

for cfg in slide_configs:
    slide = prs.slides.add_slide(blank_layout)
    add_header(slide, cfg["title"])
    
    # Attach Speaker Notes
    notes_slide = slide.notes_slide
    notes_slide.notes_text_frame.text = cfg["notes"]
    
    # Generate content based on layout configuration
    if cfg["content_type"] == "bullets":
        # Left Panel styling container
        container = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.6), Inches(11.833), Inches(4.8))
        container.fill.solid()
        container.fill.fore_color.rgb = COLOR_LIGHT_BG
        container.line.fill.background()
        
        # Text Frame within Container
        text_box = slide.shapes.add_textbox(Inches(1.0), Inches(1.8), Inches(11.333), Inches(4.4))
        tf = text_box.text_frame
        tf.word_wrap = True
        
        for i, b_text in enumerate(cfg["bullets"]):
            p = tf.add_paragraph() if i > 0 else tf.paragraphs[0]
            p.text = "• " + b_text
            p.space_after = Pt(22)
            p.font.name = FONT_NAME
            p.font.size = Pt(18)
            p.font.color.rgb = COLOR_TEXT
            
    elif cfg["content_type"] == "grid":
        # 3 Column Process Block Design
        for col_idx, (g_title, g_desc) in enumerate(cfg["grid_items"]):
            col_width = Inches(3.6)
            col_gap = Inches(0.5)
            left_pos = Inches(0.75) + (col_idx * (col_width + col_gap))
            
            # Card shape
            card = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, left_pos, Inches(1.8), col_width, Inches(4.4))
            card.fill.solid()
            card.fill.fore_color.rgb = COLOR_LIGHT_BG
            card.line.color.rgb = COLOR_TEAL
            card.line.width = Pt(1.5)
            
            # Text Inside Card
            tb = slide.shapes.add_textbox(left_pos + Inches(0.2), Inches(2.0), col_width - Inches(0.4), Inches(4.0))
            tf = tb.text_frame
            tf.word_wrap = True
            
            # Card Header
            p_head = tf.paragraphs[0]
            p_head.text = g_title
            p_head.font.name = FONT_NAME
            p_head.font.size = Pt(18)
            p_head.font.bold = True
            p_head.font.color.rgb = COLOR_NAVY
            p_head.space_after = Pt(14)
            
            # Card Desc
            p_desc = tf.add_paragraph()
            p_desc.text = g_desc
            p_desc.font.name = FONT_NAME
            p_desc.font.size = Pt(14)
            p_desc.font.color.rgb = COLOR_TEXT
            p_desc.space_after = Pt(10)

    elif cfg["content_type"] == "math":
        # Linear Process blocks displaying formulas
        for block_idx, (m_title, m_formula, m_desc) in enumerate(cfg["math_items"]):
            top_pos = Inches(1.5) + (block_idx * Inches(1.7))
            
            # Colored Indicator block
            ind = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.75), top_pos, Inches(0.15), Inches(1.4))
            ind.fill.solid()
            ind.fill.fore_color.rgb = COLOR_TEAL
            ind.line.fill.background()
            
            # Text container
            tb = slide.shapes.add_textbox(Inches(1.1), top_pos, Inches(11.3), Inches(1.4))
            tf = tb.text_frame
            tf.word_wrap = True
            
            p_title = tf.paragraphs[0]
            p_title.text = m_title
            p_title.font.name = FONT_NAME
            p_title.font.size = Pt(15)
            p_title.font.bold = True
            p_title.font.color.rgb = COLOR_NAVY
            
            p_formula = tf.add_paragraph()
            p_formula.text = m_formula
            p_formula.font.name = "Consolas" # Monospace look for equations
            p_formula.font.size = Pt(18)
            p_formula.font.bold = True
            p_formula.font.color.rgb = COLOR_TEAL
            p_formula.space_before = Pt(4)
            p_formula.space_after = Pt(4)
            
            p_desc = tf.add_paragraph()
            p_desc.text = m_desc
            p_desc.font.name = FONT_NAME
            p_desc.font.size = Pt(13)
            p_desc.font.color.rgb = COLOR_TEXT

    elif cfg["content_type"] == "table_recognition":
        # Native PowerPoint Table insertion
        rows, cols = 6, 8
        left, top, width, height = Inches(0.75), Inches(1.8), Inches(11.833), Inches(4.4)
        table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
        table = table_shape.table
        
        headers = ["Threshold", "True Pos (TP)", "True Neg (TN)", "False Pos (FP)", "False Neg (FN)", "Accuracy", "FAR", "FRR"]
        data = [
            ["0.30", "100", "85", "15", "0", "92.5%", "15.0%", "0.0%"],
            ["0.35", "100", "94", "6", "0", "97.0%", "6.0%", "0.0%"],
            ["0.40 (Optimal)", "98", "100", "0", "2", "99.0%", "0.0%", "2.0%"],
            ["0.45 (Optimal)", "95", "100", "0", "5", "97.5%", "0.0%", "5.0%"],
            ["0.50", "82", "100", "0", "18", "91.0%", "0.0%", "18.0%"]
        ]
        
        # Populate headers
        for col_idx, header in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.text = header
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_NAVY
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            p.font.name = FONT_NAME
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = RGBColor(255, 255, 255)
            
        # Populate rows
        for row_idx, row_data in enumerate(data):
            for col_idx, val in enumerate(row_data):
                cell = table.cell(row_idx + 1, col_idx)
                cell.text = val
                cell.fill.solid()
                
                # Highlight optimal rows
                if "Optimal" in row_data[0]:
                    cell.fill.fore_color.rgb = RGBColor(209, 250, 229) # Mint green shade
                else:
                    cell.fill.fore_color.rgb = COLOR_LIGHT_BG
                    
                p = cell.text_frame.paragraphs[0]
                p.alignment = PP_ALIGN.CENTER
                p.font.name = FONT_NAME
                p.font.size = Pt(13)
                if "Optimal" in row_data[0]:
                    p.font.bold = True
                    p.font.color.rgb = COLOR_TEAL
                else:
                    p.font.color.rgb = COLOR_TEXT

    elif cfg["content_type"] == "table_latency":
        # Metrics Table Comparison
        rows, cols = 3, 4
        left, top, width, height = Inches(0.75), Inches(2.2), Inches(11.833), Inches(3.0)
        table_shape = slide.shapes.add_table(rows, cols, left, top, width, height)
        table = table_shape.table
        
        headers = ["Architecture Model", "Average FPS", "UI Responsiveness", "Hardware Drivers"]
        data = [
            ["Single-Threaded Baseline", "4.2 FPS", "Unresponsive (Severe lagging)", "MSMF Default Engine"],
            ["Asynchronous Multithreaded", "32.5 FPS", "Highly Responsive (Fluid)", "DirectShow Bypass Driver"]
        ]
        
        # Populate headers
        for col_idx, header in enumerate(headers):
            cell = table.cell(0, col_idx)
            cell.text = header
            cell.fill.solid()
            cell.fill.fore_color.rgb = COLOR_NAVY
            p = cell.text_frame.paragraphs[0]
            p.alignment = PP_ALIGN.CENTER
            p.font.name = FONT_NAME
            p.font.size = Pt(14)
            p.font.bold = True
            p.font.color.rgb = RGBColor(255, 255, 255)
            
        # Populate rows
        for row_idx, row_data in enumerate(data):
            for col_idx, val in enumerate(row_data):
                cell = table.cell(row_idx + 1, col_idx)
                cell.text = val
                cell.fill.solid()
                if "Asynchronous" in row_data[0]:
                    cell.fill.fore_color.rgb = RGBColor(209, 250, 229)
                else:
                    cell.fill.fore_color.rgb = COLOR_LIGHT_BG
                    
                p = cell.text_frame.paragraphs[0]
                p.alignment = PP_ALIGN.CENTER
                p.font.name = FONT_NAME
                p.font.size = Pt(13)
                if "Asynchronous" in row_data[0]:
                    p.font.bold = True
                    p.font.color.rgb = COLOR_TEAL
                else:
                    p.font.color.rgb = COLOR_TEXT
                    
    elif cfg["content_type"] == "placeholder_image":
        # Add visual box indicating screenshot layout instruction
        p_box = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.8), Inches(11.833), Inches(4.5))
        p_box.fill.solid()
        p_box.fill.fore_color.rgb = COLOR_LIGHT_BG
        p_box.line.color.rgb = COLOR_TEAL
        p_box.line.width = Pt(1.5)
        p_box.line.dash_style = 2 # Dashed line
        
        tb = slide.shapes.add_textbox(Inches(1.0), Inches(3.6), Inches(11.333), Inches(1.0))
        p = tb.text_frame.paragraphs[0]
        p.text = cfg["placeholder_text"]
        p.alignment = PP_ALIGN.CENTER
        p.font.name = FONT_NAME
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = COLOR_TEXT

    elif cfg["content_type"] == "grid_dual":
        # Left Container
        box1 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.75), Inches(1.6), Inches(5.6), Inches(4.8))
        box1.fill.solid()
        box1.fill.fore_color.rgb = COLOR_LIGHT_BG
        box1.line.fill.background()
        
        # Left Text frame
        tb1 = slide.shapes.add_textbox(Inches(0.95), Inches(1.8), Inches(5.2), Inches(4.4))
        tf1 = tb1.text_frame
        tf1.word_wrap = True
        
        p_h1 = tf1.paragraphs[0]
        p_h1.text = cfg["col1_title"]
        p_h1.font.name = FONT_NAME
        p_h1.font.size = Pt(18)
        p_h1.font.bold = True
        p_h1.font.color.rgb = COLOR_NAVY
        p_h1.space_after = Pt(14)
        
        for bullet in cfg["col1_bullets"]:
            p = tf1.add_paragraph()
            p.text = "• " + bullet
            p.font.name = FONT_NAME
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(12)
            
        # Right Container
        box2 = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.983), Inches(1.6), Inches(5.6), Inches(4.8))
        box2.fill.solid()
        box2.fill.fore_color.rgb = COLOR_LIGHT_BG
        box2.line.color.rgb = COLOR_TEAL
        box2.line.width = Pt(1.5)
        
        # Right Text frame
        tb2 = slide.shapes.add_textbox(Inches(7.183), Inches(1.8), Inches(5.2), Inches(4.4))
        tf2 = tb2.text_frame
        tf2.word_wrap = True
        
        p_h2 = tf2.paragraphs[0]
        p_h2.text = cfg["col2_title"]
        p_h2.font.name = FONT_NAME
        p_h2.font.size = Pt(18)
        p_h2.font.bold = True
        p_h2.font.color.rgb = COLOR_TEAL
        p_h2.space_after = Pt(14)
        
        for bullet in cfg["col2_bullets"]:
            p = tf2.add_paragraph()
            p.text = "• " + bullet
            p.font.name = FONT_NAME
            p.font.size = Pt(13)
            p.font.color.rgb = COLOR_TEXT
            p.space_after = Pt(12)

# Create Title slide as Slide 1
title_slide = create_title_slide(
    prs, 
    title="Design and Implementation of an Offline, Edge-AI Based Face Recognition Attendance System with Liveness Detection",
    subtitle="A High-Speed, Decentralized Biometric Verification and Auditing Platform for Academic Environments",
    presenter="Goodness Adewuyi",
    dept="Computer Science, Ladoke Akintola University of Technology",
    supervisor="Department Supervisor Panel"
)

# Put title slide at the absolute beginning
# Slide elements have been naturally ordered by appending sequence
prs.slides._sldIdLst.insert(0, prs.slides._sldIdLst[-1])

# Save completed PowerPoint file
filename = "LAUTECH_Attendance_Defense.pptx"
prs.save(filename)
print(f"[SUCCESS] Enterprise-grade presentation document saved as: {os.path.abspath(filename)}")