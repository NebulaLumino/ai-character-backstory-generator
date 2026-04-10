import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "AI Food Label Nutrition Analyzer",
  description: "Understand nutrition labels, interpret serving sizes, and evaluate food products",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className="bg-gray-900 text-white">{children}</body>
    </html>
  );
}