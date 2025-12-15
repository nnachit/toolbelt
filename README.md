# ToolBelt

A collection of developer utilities built with SvelteKit and Django.

## Tech Stack

- **Frontend**: SvelteKit 2, Svelte 5, Tailwind CSS 4
- **Backend**: Django 5, Django REST Framework

## Getting Started

```bash
# Backend
cd backend
pip install -r requirements.txt
python manage.py runserver

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

Open http://localhost:5173

## Tools

### Available

- [x] **Password Generator** - Generate secure random passwords with customizable length and character types

### Planned

#### Encoding & Decoding
- [ ] **Base64 Encoder/Decoder** - Encode and decode Base64 strings
- [ ] **URL Encoder/Decoder** - Encode and decode URL components
- [ ] **HTML Entity Encoder** - Convert special characters to HTML entities

#### Hashing
- [ ] **Hash Generator** - Generate MD5, SHA-1, SHA-256, SHA-512 hashes
- [ ] **Bcrypt Generator** - Hash passwords with bcrypt
- [ ] **Hash Identifier** - Identify hash types from hash strings

#### Generators
- [ ] **UUID Generator** - Generate UUID v1, v4, v7
- [ ] **Lorem Ipsum Generator** - Generate placeholder text
- [ ] **Random Number Generator** - Generate random numbers with constraints
- [ ] **Fake Data Generator** - Generate fake names, emails, addresses

#### Formatters & Validators
- [ ] **JSON Formatter** - Format, validate, and minify JSON
- [ ] **JavaScript Formatter** - Format and beautify JavaScript code
- [ ] **CSS Formatter** - Format and beautify CSS code
- [ ] **HTML Formatter** - Format and beautify HTML code
- [ ] **XML Formatter** - Format and validate XML
- [ ] **SQL Formatter** - Format SQL queries
- [ ] **YAML Formatter** - Format and validate YAML
- [ ] **Regex Tester** - Test regular expressions with live preview
- [ ] **Cron Expression Parser** - Parse and validate cron expressions
- [ ] **JSON to YAML Converter** - Convert between JSON and YAML

#### Converters
- [ ] **Unix Timestamp Converter** - Convert between timestamps and dates
- [ ] **Color Converter** - Convert between HEX, RGB, HSL
- [ ] **Number Base Converter** - Convert between binary, octal, decimal, hex
- [ ] **Unit Converter** - Convert bytes, time, length, etc.

#### Text Utilities
- [ ] **Case Converter** - Convert between camelCase, snake_case, UPPERCASE, etc.
- [ ] **Text Diff** - Compare two texts and highlight differences
- [ ] **Word/Character Counter** - Count words, characters, lines
- [ ] **Markdown Preview** - Live preview of markdown content

#### Security & Crypto
- [ ] **JWT Decoder** - Decode and inspect JWT tokens
- [ ] **Certificate Decoder** - Parse and display X.509 certificates
- [ ] **RSA Key Generator** - Generate RSA key pairs
- [ ] **TOTP Generator** - Generate time-based one-time passwords

#### Code Playgrounds
- [ ] **HTML/CSS/JS Playground** - Live preview of HTML, CSS, and JavaScript
- [ ] **Markdown Editor** - Write markdown with live preview
- [ ] **SVG Editor** - Edit and preview SVG code
- [ ] **Tailwind Playground** - Test Tailwind CSS classes live

#### Network
- [ ] **IP Address Info** - Get details about an IP address
- [ ] **HTTP Status Codes** - Reference for HTTP status codes
- [ ] **User Agent Parser** - Parse and analyze user agent strings

#### Image Tools
- [ ] **Base64 Image Encoder** - Convert images to/from Base64
- [ ] **Favicon Generator** - Generate favicons from images
- [ ] **Placeholder Image** - Generate placeholder images with custom size/color

#### QR & Barcodes
- [ ] **QR Code Generator** - Generate QR codes from text/URLs
- [ ] **Barcode Generator** - Generate various barcode formats

#### API & HTTP
- [ ] **API Tester** - Send HTTP requests and view responses (like Postman)
- [ ] **HTTP Headers Parser** - Parse and explain HTTP headers
- [ ] **CORS Checker** - Test CORS configuration for URLs
- [ ] **Webhook Tester** - Generate temporary endpoints to test webhooks
- [ ] **cURL Converter** - Convert cURL commands to code (JS, Python, etc.)
- [ ] **OpenAPI Viewer** - View and explore OpenAPI/Swagger specs

#### Database Tools
- [ ] **SQL to NoSQL Converter** - Convert SQL queries to MongoDB queries
- [ ] **Database Schema Designer** - Design database schemas visually
- [ ] **Connection String Parser** - Parse and build database connection strings

#### Git & Version Control
- [ ] **Git Command Generator** - Build complex git commands interactively
- [ ] **.gitignore Generator** - Generate .gitignore for various languages/frameworks
- [ ] **Commit Message Generator** - Generate conventional commit messages

#### DevOps & Config
- [ ] **Docker Compose Generator** - Build docker-compose.yml interactively
- [ ] **Nginx Config Generator** - Generate nginx configuration files
- [ ] **Environment Variables Editor** - Edit and manage .env files
- [ ] **Package.json Generator** - Create package.json interactively

#### Data & Serialization
- [ ] **CSV to JSON Converter** - Convert between CSV and JSON
- [ ] **JSON to TypeScript** - Generate TypeScript interfaces from JSON
- [ ] **JSON to Go Struct** - Generate Go structs from JSON
- [ ] **JSON to Python Class** - Generate Python dataclasses from JSON
- [ ] **XML to JSON Converter** - Convert between XML and JSON

#### String & Data Manipulation
- [ ] **String Escape/Unescape** - Escape strings for various languages
- [ ] **Slug Generator** - Generate URL-friendly slugs
- [ ] **Truncate Text** - Truncate text with ellipsis options
- [ ] **Remove Duplicates** - Remove duplicate lines from text
- [ ] **Sort Lines** - Sort lines alphabetically or numerically

#### Math & Numbers
- [ ] **Percentage Calculator** - Calculate percentages
- [ ] **Byte Calculator** - Convert between KB, MB, GB, TB
- [ ] **Aspect Ratio Calculator** - Calculate aspect ratios for images/videos

#### Date & Time
- [ ] **Timezone Converter** - Convert times between timezones
- [ ] **Date Difference Calculator** - Calculate difference between dates
- [ ] **ISO 8601 Formatter** - Format dates to ISO 8601

#### Frontend Specific
- [ ] **CSS Gradient Generator** - Generate CSS gradients visually
- [ ] **Box Shadow Generator** - Generate CSS box shadows
- [ ] **Border Radius Generator** - Generate CSS border radius
- [ ] **Flexbox Playground** - Learn and test CSS flexbox
- [ ] **Grid Playground** - Learn and test CSS grid
- [ ] **Media Query Generator** - Generate responsive media queries
- [ ] **Meta Tags Generator** - Generate HTML meta tags for SEO
- [ ] **Open Graph Generator** - Generate Open Graph meta tags
- [ ] **Sprite Sheet Generator** - Combine images into sprite sheets

#### Backend Specific
- [ ] **API Rate Limit Calculator** - Calculate API rate limits
- [ ] **Load Time Estimator** - Estimate page load times
- [ ] **Regex to Code** - Generate regex code for various languages

## Project Structure

```
toolbelt/
├── backend/
│   ├── backend/           # Django project settings
│   └── password_generator/  # Password generator app
└── frontend/
    └── src/
        └── routes/        # SvelteKit pages
```

## License

MIT
