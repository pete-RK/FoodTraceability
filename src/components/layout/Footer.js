import React from 'react';
import '../../styles/Footer.css'; 
const Footer = () => {
    return (
        <footer className="site-footer">
            <div className="footer-content">
                <p>&copy; {new Date().getFullYear()} Agriculture Food Tracebility. All rights reserved.</p>
                <div className="footer-links">
                    <a href="/privacy-policy">Privacy Policy</a>
                    <a href="/terms-of-service">Terms of Service</a>
                    <a href="/contact">Contact Us</a>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
