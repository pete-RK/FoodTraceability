import React from 'react';
import '../../styles/Header.css'; 

const Header = () => {
    return (
        <header className="site-header">
            <div className="logo">
                <h1>Agriculture Food Tracebility</h1>
            </div>
            <nav className="main-nav">
                <ul>
                    <li><a href="/">Home</a></li>
                    <li><a href="/about">About</a></li>
                    <li><a href="/services">Services</a></li>
                    <li><a href="/contact">Contact</a></li>
                </ul>
            </nav>
        </header>
    );
};

export default Header;
