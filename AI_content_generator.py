import streamlit as st
import os
from dotenv import load_dotenv
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    """
    Inisialisasi Google AI dengan cache
    """
    try:
        # Load environment variables
        load_dotenv()
        
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            st.error("⚠️ Google API Key tidak ditemukan! Silakan tambahkan ke file .env")
            st.stop()
        
        # Configure Google AI
        genai.configure(api_key=api_key)
        
        # Initialize model
        model = genai.GenerativeModel('gemini-2.5-flash')
        return model
    except Exception as e:
        st.error(f"❌ Error saat menginisialisasi Google AI: {str(e)}")
        st.stop()

def generate_content(topic, model):
    """
    Generate konten menggunakan Google Gemini AI
    """
    try:
        # Prompt template untuk AI
        prompt = f"""
        Buatkan konten yang menarik dan informatif tentang topik: "{topic}"
        
        Format konten:
        1. Judul yang catchy
        2. Pendahuluan singkat
        3. 3-5 poin utama dengan penjelasan
        4. Kesimpulan
        5. Call to action
        
        Konten harus:
        - Mudah dipahami
        - Informatif dan berguna
        - Engaging untuk pembaca
        - Panjang sekitar 200-300 kata
        
        Gunakan bahasa Indonesia yang baik dan benar.
        """
        
        # Generate menggunakan Google AI
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"❌ Terjadi error saat generate konten: {str(e)}"

def run():
    """
    AI Content Generator - Ultra Modern Edition
    """
    
    # Konfigurasi halaman
    st.set_page_config(
        page_title="AI Content Generator Pro",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Custom CSS dengan animasi dan efek premium
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=Space+Grotesk:wght@700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
        /* Main Background dengan Animated Particles */
        .main {
            background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
            position: relative;
            overflow: hidden;
        }
        
        .main::before {
            content: '';
            position: absolute;
            width: 300%;
            height: 300%;
            background: radial-gradient(circle, rgba(99, 102, 241, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: moveBackground 20s linear infinite;
            z-index: 0;
        }
        
        @keyframes moveBackground {
            0% { transform: translate(0, 0); }
            100% { transform: translate(50px, 50px); }
        }
        
        .block-container {
            padding-top: 2rem;
            padding-bottom: 3rem;
            position: relative;
            z-index: 1;
        }
        
        /* Floating particles effect */
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
        
        /* Hero Section Ultra Modern */
        .hero-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            background-size: 200% 200%;
            animation: gradientShift 8s ease infinite;
            padding: 4rem 2rem;
            border-radius: 30px;
            margin-bottom: 3rem;
            box-shadow: 0 30px 90px rgba(102, 126, 234, 0.4), 
                        0 0 0 1px rgba(255, 255, 255, 0.1),
                        inset 0 0 100px rgba(255, 255, 255, 0.05);
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        
        @keyframes gradientShift {
            0%, 100% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
        }
        
        /* Glowing orbs */
        .hero-container::before,
        .hero-container::after {
            content: '';
            position: absolute;
            border-radius: 50%;
            filter: blur(80px);
            opacity: 0.3;
            animation: float 6s ease-in-out infinite;
        }
        
        .hero-container::before {
            width: 300px;
            height: 300px;
            background: rgba(255, 255, 255, 0.3);
            top: -100px;
            left: -100px;
        }
        
        .hero-container::after {
            width: 250px;
            height: 250px;
            background: rgba(240, 147, 251, 0.4);
            bottom: -80px;
            right: -80px;
            animation-delay: 3s;
        }
        
        .hero-content {
            position: relative;
            z-index: 1;
        }
        
        .hero-title {
            font-family: 'Space Grotesk', sans-serif;
            color: white;
            font-size: 4rem;
            font-weight: 900;
            margin: 0;
            text-shadow: 0 0 40px rgba(255, 255, 255, 0.5),
                         0 5px 15px rgba(0, 0, 0, 0.3);
            letter-spacing: -2px;
            animation: fadeInScale 1s ease;
            line-height: 1.1;
        }
        
        @keyframes fadeInScale {
            0% {
                opacity: 0;
                transform: scale(0.8);
            }
            100% {
                opacity: 1;
                transform: scale(1);
            }
        }
        
        .hero-subtitle {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.3rem;
            margin-top: 1.5rem;
            font-weight: 400;
            animation: fadeInUp 1.2s ease;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }
        
        .hero-badge {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(20px);
            padding: 0.8rem 2rem;
            border-radius: 50px;
            color: white;
            font-weight: 700;
            margin-top: 1.5rem;
            border: 2px solid rgba(255, 255, 255, 0.25);
            animation: fadeInUp 1.4s ease, pulse 2s ease-in-out infinite;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            font-size: 1.05rem;
        }
        
        @keyframes pulse {
            0%, 100% { box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2); }
            50% { box-shadow: 0 8px 40px rgba(255, 255, 255, 0.3); }
        }
        
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(40px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        /* Stats Cards dengan Glassmorphism */
        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin: 3rem 0;
        }
        
        .stat-card {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.1);
            padding: 2rem;
            border-radius: 25px;
            text-align: center;
            color: white;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3),
                        inset 0 0 0 1px rgba(255, 255, 255, 0.05);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .stat-card::before {
            content: '';
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
            transform: rotate(45deg);
            transition: all 0.5s;
        }
        
        .stat-card:hover {
            transform: translateY(-10px) scale(1.03);
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
            border-color: rgba(102, 126, 234, 0.5);
        }
        
        .stat-card:hover::before {
            left: 100%;
        }
        
        .stat-number {
            font-size: 3.5rem;
            margin: 0;
            animation: bounce 3s infinite;
            filter: drop-shadow(0 0 20px currentColor);
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-15px); }
        }
        
        .stat-label {
            font-size: 1.1rem;
            font-weight: 600;
            margin-top: 1rem;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        
        /* Feature Cards Premium */
        .feature-card {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.1);
            padding: 2.5rem;
            border-radius: 25px;
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
            margin-bottom: 2rem;
            transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            position: relative;
            overflow: hidden;
        }
        
        .feature-card::before {
            content: '';
            position: absolute;
            inset: 0;
            background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(240, 147, 251, 0.1));
            opacity: 0;
            transition: opacity 0.5s;
        }
        
        .feature-card:hover {
            transform: translateY(-15px) scale(1.03);
            box-shadow: 0 25px 70px rgba(102, 126, 234, 0.5);
            border-color: rgba(102, 126, 234, 0.6);
        }
        
        .feature-card:hover::before {
            opacity: 1;
        }
        
        .feature-icon {
            font-size: 4rem;
            margin-bottom: 1.5rem;
            display: inline-block;
            filter: drop-shadow(0 0 30px currentColor);
            animation: rotate360 20s linear infinite;
        }
        
        @keyframes rotate360 {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
        
        .feature-title {
            color: white;
            font-size: 1.7rem;
            font-weight: 700;
            margin: 1rem 0;
            text-shadow: 0 2px 20px rgba(102, 126, 234, 0.5);
        }
        
        .feature-text {
            color: rgba(255, 255, 255, 0.8);
            line-height: 1.8;
            font-size: 1.05rem;
        }
        
        /* Input Container dengan Glow Effect */
        .input-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.1);
            padding: 3rem;
            border-radius: 30px;
            box-shadow: 0 15px 50px rgba(0, 0, 0, 0.3);
            margin: 3rem 0;
            position: relative;
            overflow: hidden;
        }
        
        .input-container::before {
            content: '';
            position: absolute;
            inset: -2px;
            background: linear-gradient(45deg, #667eea, #764ba2, #f093fb, #4facfe);
            background-size: 400%;
            animation: gradientRotate 10s linear infinite;
            border-radius: 30px;
            z-index: -1;
            opacity: 0.5;
            filter: blur(10px);
        }
        
        @keyframes gradientRotate {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        .input-label {
            color: white;
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            display: block;
            text-shadow: 0 2px 20px rgba(102, 126, 234, 0.5);
        }
        
        /* Input Field Modern */
        .stTextInput > div > div > input {
            border-radius: 15px;
            border: 2px solid rgba(102, 126, 234, 0.5);
            padding: 1rem 1.5rem;
            font-size: 1rem;
            transition: all 0.4s ease;
            background: rgba(15, 12, 41, 0.6);
            backdrop-filter: blur(10px);
            color: white;
            box-shadow: 0 5px 25px rgba(0, 0, 0, 0.3);
        }
        
        .stTextInput > div > div > input::placeholder {
            color: rgba(255, 255, 255, 0.5);
        }
        
        .stTextInput > div > div > input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3),
                        0 8px 30px rgba(102, 126, 234, 0.4);
            transform: translateY(-2px);
            background: rgba(15, 12, 41, 0.8);
        }
        
        /* Button Ultra Modern */
        .stButton > button {
            width: 100%;
            border-radius: 20px;
            padding: 1.5rem 2rem;
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            box-shadow: 0 10px 40px rgba(102, 126, 234, 0.5);
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            color: white;
            text-transform: uppercase;
            letter-spacing: 2px;
            position: relative;
            overflow: hidden;
        }
        
        .stButton > button::before {
            content: '';
            position: absolute;
            top: 50%;
            left: 50%;
            width: 0;
            height: 0;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.3);
            transform: translate(-50%, -50%);
            transition: width 0.6s, height 0.6s;
        }
        
        .stButton > button:hover::before {
            width: 300%;
            height: 300%;
        }
        
        .stButton > button:hover {
            transform: translateY(-5px) scale(1.02);
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.7);
        }
        
        .stButton > button:active {
            transform: translateY(-2px) scale(0.98);
        }
        
        /* Result Container dengan Animation */
        .result-container {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(102, 126, 234, 0.3);
            padding: 3rem;
            border-radius: 30px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            margin-top: 2rem;
            animation: slideInLeft 0.8s ease;
            position: relative;
            overflow: hidden;
        }
        
        .result-container::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 6px;
            background: linear-gradient(180deg, #667eea, #764ba2, #f093fb);
            animation: gradientMove 3s ease-in-out infinite;
        }
        
        @keyframes gradientMove {
            0%, 100% { transform: translateY(-20%); }
            50% { transform: translateY(20%); }
        }
        
        @keyframes slideInLeft {
            from {
                opacity: 0;
                transform: translateX(-100px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }
        
        .result-title {
            color: white;
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 2rem;
            text-shadow: 0 2px 30px rgba(102, 126, 234, 0.5);
        }
        
        /* Topic Display */
        .topic-display {
            background: rgba(102, 126, 234, 0.15);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(102, 126, 234, 0.3);
            padding: 1.5rem;
            border-radius: 20px;
            margin-top: 1.5rem;
            animation: fadeInUp 0.5s ease;
        }
        
        /* Download Button Premium */
        .stDownloadButton > button {
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
            color: white;
            border: none;
            border-radius: 18px;
            padding: 1rem 2rem;
            font-weight: 700;
            font-size: 1.1rem;
            transition: all 0.4s ease;
            box-shadow: 0 8px 30px rgba(17, 153, 142, 0.4);
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .stDownloadButton > button:hover {
            transform: translateY(-4px) scale(1.05);
            box-shadow: 0 15px 45px rgba(17, 153, 142, 0.6);
        }
        
        /* Footer Ultra Modern */
        .footer-container {
            background: rgba(0, 0, 0, 0.4);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.1);
            padding: 3.5rem 2rem;
            border-radius: 30px;
            margin-top: 5rem;
            box-shadow: 0 -10px 50px rgba(0, 0, 0, 0.3);
            position: relative;
            overflow: hidden;
        }
        
        .footer-container::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
            background: linear-gradient(90deg, 
                transparent, 
                #667eea, 
                #764ba2, 
                #f093fb, 
                transparent);
        }
        
        .footer-content {
            text-align: center;
            color: white;
        }
        
        .footer-title {
            font-size: 1.8rem;
            font-weight: 700;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, #06b6d4 0%, #67e8f9 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s ease-in-out infinite;
        }
        
        @keyframes shimmer {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.7; }
        }
        
        .footer-creator {
            font-family: 'Space Grotesk', sans-serif;
            font-size: 2.5rem;
            font-weight: 900;
            margin: 1.5rem 0;
            color: white;
            text-shadow: 0 0 40px rgba(102, 126, 234, 0.8),
                         0 5px 15px rgba(0, 0, 0, 0.5);
            letter-spacing: 2px;
            animation: glow 2s ease-in-out infinite;
        }
        
        @keyframes glow {
            0%, 100% { text-shadow: 0 0 40px rgba(102, 126, 234, 0.8), 0 5px 15px rgba(0, 0, 0, 0.5); }
            50% { text-shadow: 0 0 60px rgba(240, 147, 251, 1), 0 5px 20px rgba(0, 0, 0, 0.5); }
        }
        
        .footer-divider {
            height: 3px;
            background: linear-gradient(90deg, 
                transparent, 
                rgba(102, 126, 234, 0.5), 
                rgba(240, 147, 251, 0.5), 
                transparent);
            margin: 2rem auto;
            max-width: 60%;
            border-radius: 10px;
        }
        
        .footer-tech {
            display: flex;
            justify-content: center;
            gap: 1.2rem;
            flex-wrap: wrap;
            margin-top: 2rem;
        }
        
        .tech-badge {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border: 2px solid rgba(255, 255, 255, 0.2);
            padding: 0.8rem 1.5rem;
            border-radius: 25px;
            font-size: 1rem;
            font-weight: 600;
            color: white;
            transition: all 0.3s ease;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.2);
        }
        
        .tech-badge:hover {
            background: rgba(102, 126, 234, 0.3);
            border-color: rgba(102, 126, 234, 0.5);
            transform: translateY(-5px) scale(1.05);
            box-shadow: 0 10px 30px rgba(102, 126, 234, 0.4);
        }
        
        .footer-year {
            font-size: 1rem;
            opacity: 0.7;
            margin-top: 2rem;
            font-weight: 500;
        }
        
        /* Alert Styling */
        .stAlert {
            border-radius: 20px;
            border: none;
            backdrop-filter: blur(10px);
            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
        }
        
        /* Spinner Custom */
        .stSpinner > div {
            border-color: #667eea !important;
        }
        
        /* Success Message */
        .success-message {
            animation: successBounce 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        
        @keyframes successBounce {
            0% { transform: scale(0.3); opacity: 0; }
            50% { transform: scale(1.1); }
            100% { transform: scale(1); opacity: 1; }
        }
        </style>
    """, unsafe_allow_html=True)
    
    # Hero Header
    st.markdown("""
        <div class="hero-container">
            <div class="hero-content">
                <h1 class="hero-title">🚀 AI Content Generator Pro</h1>
                <p class="hero-subtitle">Ubah Ide Anda Menjadi Konten Menarik dengan Kekuatan Kecerdasan Buatan</p>
                <div class="hero-badge">✨ Didukung oleh Google Gemini AI</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Inisialisasi Google AI
    model = init_google_ai()
    
    # Stats Section
    st.markdown("""
        <div class="stats-container">
            <div class="stat-card">
                <p class="stat-number">⚡</p>
                <p class="stat-label">Generasi Super Cepat</p>
            </div>
            <div class="stat-card">
                <p class="stat-number">🎯</p>
                <p class="stat-label">100% Akurat & Berkualitas</p>
            </div>
            <div class="stat-card">
                <p class="stat-number">✨</p>
                <p class="stat-label">Teknologi AI Premium</p>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Main Input Section
    st.markdown("""
        <div class="input-container">
            <span class="input-label">📝 Masukkan Topik Konten Anda</span>
        </div>
    """, unsafe_allow_html=True)
    
    col_input, col_button = st.columns([3, 1], gap="medium")
    
    with col_input:
        user_topic = st.text_input(
            "",
            placeholder="Contoh: Tips Belajar Python untuk Pemula, Manfaat AI dalam Bisnis Modern, Strategi Digital Marketing 2025...",
            label_visibility="collapsed"
        )
    
    with col_button:
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("🔥 GENERATE", type="primary")
    
    if user_topic:
        st.markdown(f"""
            <div class="topic-display">
                <span style="color: rgba(255, 255, 255, 0.8); font-weight: 600; font-size: 1rem;">📌 Topik Terpilih:</span>
                <br>
                <span style="color: white; font-weight: 800; font-size: 1.3rem; text-shadow: 0 2px 20px rgba(240, 147, 251, 0.5);"> {user_topic}</span>
            </div>  
        """, unsafe_allow_html=True)
    
    # Generate Content
    if generate_btn:
        if not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu!")
        else:
            with st.spinner("🤖 AI sedang bekerja keras membuat konten masterpiece untuk Anda..."):
                hasil_konten = generate_content(user_topic, model)
            
            # Display Result with animation
            st.balloons()
            st.markdown('<div class="success-message">', unsafe_allow_html=True)
            st.success("✅ Konten berhasil dibuat dengan sempurna!")
            st.markdown('</div>', unsafe_allow_html=True)
            
            st.markdown("""
                <div class="result-container">
                    <h2 class="result-title">📄 Hasil Konten Premium Anda</h2>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="background: rgba(102, 126, 234, 0.15); 
                            padding: 2.5rem; 
                            border-radius: 20px; 
                            line-height: 1.9; 
                            color: #ecfdf5;
                            box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
                            border: 2px solid rgba(102, 126, 234, 0.2);
                            font-size: 1.05rem;">
                    {hasil_konten.replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            # Download button
            st.markdown("<br>", unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                st.download_button(
                    label="📥 Download Konten (.txt)",
                    data=hasil_konten,
                    file_name=f"konten_{user_topic.replace(' ', '_')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
    
    # Footer Section
    st.markdown("""
        <div class="footer-container">
            <div class="footer-content">
                <p class="footer-title">Created with by</p>
                <h2 class="footer-creator">MUHAMMAD RIZKY MAULANA <br>AI Content Generator Pro</h2>
                <div class="footer-divider"></div>
                <div class="footer-tech">
                    <span class="tech-badge">🐍 Python</span>
                    <span class="tech-badge">🎨 Streamlit</span>
                    <span class="tech-badge">🤖 Google Gemini AI</span>
                    <span class="tech-badge">✨ Modern CSS3</span>
                    <span class="tech-badge">🚀 Advanced Animations</span>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    run()