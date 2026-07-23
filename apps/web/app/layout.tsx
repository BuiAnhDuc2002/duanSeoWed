import type { Metadata } from "next";
import "./styles.css";

export const metadata: Metadata = {
  title: "AI SEO Clinic",
  description: "Quản trị nền tảng AI SEO có kiểm duyệt y khoa",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="vi">
      <body>{children}</body>
    </html>
  );
}

