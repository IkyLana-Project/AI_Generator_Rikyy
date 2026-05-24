import streamlit as st
import os
import google.generativeai as genai

@st.cache_resource
def init_google_ai():
    """
    Inisialisasi Google AI dengan prioritas Streamlit Secrets
    """
    try:
        # 1. Prioritas utama: Coba ambil dari Streamlit Secrets
        if "GOOGLE_API_KEY" in st.secrets:
            api_key = st.secrets["GOOGLE_API_KEY"]
            
        # 2. Alternatif: Jika dijalankan di komputer lokal (butuh dotenv)
        else:
            try:
                from dotenv import load_dotenv
                load_dotenv()
            except ImportError:
                pass # Abaikan jika tidak ada dotenv di Cloud
                
            api_key = os.getenv("GOOGLE_API_KEY")
            
        # Pengecekan akhir apakah key berhasil didapat
        if not api_key:
            st.error("⚠️ Google API Key tidak ditemukan! Silakan cek Settings > Secrets di Streamlit Cloud.")
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
        
        response = model.generate_content(prompt)
        return response.text
    
    except Exception as e:
        return f"❌ Terjadi error saat generate konten: {str(e)}"

def run():
    """
    AI Content Generator - Ultra Modern Edition
    """
    
    st.set_page_config(
        page_title="AI Content Generator Pro",
        page_icon="🚀",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;900&family=Space+Grotesk:wght@700&display=swap');
        
        * {
            font-family: 'Inter', sans-serif;
        }
        
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
        
        @keyframes float {
            0%, 100% { transform: translateY(0px) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }
        
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
        
        .hero-title {
            font-family: 'Space Grotesk', sans-serif;
            color: white;
            font-size: 4rem;
            font-weight: 900;
            margin: 0;
            text-shadow: 0 0 40px rgba(255, 255, 255, 0.5),
                         0 5px 15px rgba(0, 0, 0, 0.3);
            letter-spacing: -2px;
            line-height: 1.1;
        }
        
        .hero-subtitle {
            color: rgba(255, 255, 255, 0.95);
            font-size: 1.3rem;
            margin-top: 1.5rem;
            font-weight: 400;
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
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
            font-size: 1.05rem;
        }
        
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
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        .stat-number {
            font-size: 3.5rem;
            margin: 0;
        }
        
        .stat-label {
            font-size: 1.1rem;
            font-weight: 600;
            margin-top: 1rem;
        }
        
        .input-container {
            background: rgba(255, 255, 255, 0.05);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(255, 255, 255, 0.1);
            padding: 3rem;
            border-radius: 30px;
            margin: 3rem 0;
        }
        
        .input-label {
            color: white;
            font-size: 1.6rem;
            font-weight: 700;
            margin-bottom: 1.5rem;
            display: block;
        }
        
        .stTextInput > div > div > input {
            border-radius: 15px;
            border: 2px solid rgba(102, 126, 234, 0.5);
            padding: 1rem 1.5rem;
            background: rgba(15, 12, 41, 0.6);
            color: white;
        }
        
        .stButton > button {
            width: 100%;
            border-radius: 20px;
            padding: 1.5rem 2rem;
            font-size: 1.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: none;
            color: white;
        }
        
        .result-container {
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(20px);
            border: 2px solid rgba(102, 126, 234, 0.3);
            padding: 3rem;
            border-radius: 30px;
            margin-top: 2rem;
        }
        
        .result-title {
            color: white;
            font-size: 2.2rem;
            font-weight: 800;
            margin-bottom: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
        <div class="hero-container">
            <div class="hero-content">
                <h1 class="hero-title">🚀 AI Content Generator Pro</h1>
                <p class="hero-subtitle">Ubah Ide Anda Menjadi Konten Menarik dengan Kekuatan Kecerdasan Buatan</p>
                <div class="hero-badge">✨ Didukung oleh Google Gemini AI</div>
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    model = init_google_ai()
    
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
    
    st.markdown("""
        <div class="input-container">
            <span class="input-label">📝 Masukkan Topik Konten Anda</span>
        </div>
    """, unsafe_allow_html=True)
    
    col_input, col_button = st.columns([3, 1], gap="medium")
    
    with col_input:
        user_topic = st.text_input(
            "Topik",
            placeholder="Contoh: Tips Belajar Python untuk Pemula...",
            label_visibility="collapsed"
        )
    
    with col_button:
        st.markdown("<br>", unsafe_allow_html=True)
        generate_btn = st.button("🔥 GENERATE", type="primary")
    
    if generate_btn:
        if not user_topic.strip():
            st.warning("⚠️ Mohon masukkan topik terlebih dahulu!")
        else:
            with st.spinner("🤖 AI sedang bekerja keras membuat konten..."):
                hasil_konten = generate_content(user_topic, model)
            
            st.balloons()
            st.success("✅ Konten berhasil dibuat!")
            
            st.markdown("""
                <div class="result-container">
                    <h2 class="result-title">📄 Hasil Konten Premium Anda</h2>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown(f"""
                <div style="background: rgba(102, 126, 234, 0.15); 
                            padding: 2.5rem; 
                            border-radius: 20px; 
                            color: #ecfdf5;
                            border: 2px solid rgba(102, 126, 234, 0.2);
                            font-size: 1.05rem;">
                    {hasil_konten.replace(chr(10), '<br>')}
                </div>
            """, unsafe_allow_html=True)
            
            st.download_button(
                label="📥 Download Konten (.txt)",
                data=hasil_konten,
                file_name=f"konten_{user_topic.replace(' ', '_')}.txt",
                mime="text/plain",
                use_container_width=True
            )

if __name__ == "__main__":
    run()
