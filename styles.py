#!/usr/bin/env python
# coding: utf-8

styles = """
<style>

/* === تایتل About Me به شکل بنفش طلایی === */
.about-title {
  width: 90%;
  max-width: 1100px;
  margin: 0 auto 25px auto;
  padding: 20px 10px;
  background-color: #6A0DAD;
  color: #FFD700;
  font-weight: bold;
  font-family: 'Century Gothic', sans-serif;
  font-size: clamp(20px, 4vw, 32px);
  text-align: center;
  border-radius: 25px;
  box-shadow: 0 4px 12px rgba(106, 13, 173, 0.2);
}


/* === دکمه‌ها (fancy-button) === */
.fancy-button {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 130px;
  height: 55px;
  margin: 8px;
  background-color: transparent;
  color: #6A0DAD;
  border: 2px solid #6A0DAD;
  border-radius: 25px;
  text-align: center;
  text-decoration: none !important;
  font-size: 13px;
  font-weight: bold;
  font-family: 'Century Gothic', sans-serif;
  transition: all 0.3s ease;
}

.fancy-button:hover {
  background-color: #6A0DAD;
  color: #FFD700 !important;
  transform: scale(1.05);
  text-decoration: none !important;
}

/* === ردیف دکمه‌ها (سه‌تایی کنار هم) === */
.button-row {
  display: flex;
  justify-content: center;
  gap: 10px;
  flex-wrap: wrap;
  margin-top: 20px;
}

/* === کانتینر معرفی === */
.about-container {
  max-width: 600px;
  margin: 40px auto;
  padding: 25px 30px;
  border: 2px solid #B388EB;
  border-radius: 20px;
  background: linear-gradient(145deg, #F9F4FF, #F3E8FF);
  box-shadow: 0 8px 20px rgba(138, 43, 226, 0.15);
  text-align: center;
  font-family: 'Century Gothic', sans-serif;
  color: #4B0082;
}

.about-container p {
  font-size: 16px;
  line-height: 1.6;
}
.about-container b {
  font-size: 18px;
}

/* === ریسپانسیو موبایل === */
@media (max-width: 500px) {
  .fancy-button {
    width: 90%;
    font-size: 14px;
  }

  .button-row {
    flex-direction: column;
    align-items: center;
  }
}

</style>
"""

try:
    get_ipython().run_line_magic('store', 'styles')
except:
    pass
