export type ToolIconName =
  | 'key'
  | 'code'
  | 'link'
  | 'document'
  | 'json'
  | 'shield'
  | 'hash'
  | 'fingerprint';

export interface Tool {
  /** Route of the tool, or '#' while it is still planned. */
  href: string;
  /** Short name, used in the sidebar. */
  label: string;
  /** Full name, used on the home card and in the page title. */
  title: string;
  description: string;
  icon: ToolIconName;
  available: boolean;
}

/**
 * Single source of truth for the sidebar, the home page cards and page
 * titles. Adding a tool means adding one entry here plus its route.
 */
export const tools: Tool[] = [
  {
    href: '/password',
    label: 'Password',
    title: 'Password Generator',
    description: 'Generate secure, random passwords with customizable options.',
    icon: 'key',
    available: true
  },
  {
    href: '/base64',
    label: 'Base64',
    title: 'Base64 Encoder/Decoder',
    description: 'Encode and decode Base64 strings.',
    icon: 'code',
    available: true
  },
  {
    href: '/url-encoder',
    label: 'URL Encoder',
    title: 'URL Encoder/Decoder',
    description: 'Encode and decode URL components.',
    icon: 'link',
    available: true
  },
  {
    href: '/html-entities',
    label: 'HTML Entities',
    title: 'HTML Entity Encoder',
    description: 'Convert special characters to HTML entities.',
    icon: 'document',
    available: true
  },
  {
    href: '/json-formatter',
    label: 'JSON Formatter',
    title: 'JSON Formatter',
    description: 'Format, validate, and minify JSON.',
    icon: 'json',
    available: true
  },
  {
    href: '/jwt-decoder',
    label: 'JWT Decoder',
    title: 'JWT Decoder',
    description: 'Decode and inspect JWT tokens.',
    icon: 'shield',
    available: true
  },
  {
    href: '#',
    label: 'Hash',
    title: 'Hash Generator',
    description: 'Generate MD5, SHA-1, SHA-256 and other hash values.',
    icon: 'hash',
    available: false
  },
  {
    href: '#',
    label: 'UUID',
    title: 'UUID Generator',
    description: 'Generate random UUIDs (v4) or timestamp-based UUIDs (v1).',
    icon: 'fingerprint',
    available: false
  }
];

export function toolByPath(pathname: string): Tool | undefined {
  return tools.find((tool) => tool.available && tool.href === pathname);
}
