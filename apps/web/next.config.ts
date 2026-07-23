import type { NextConfig } from "next";

// Vercel manages the Next.js server output itself. Standalone output is only
// needed for self-hosted containers and can break tracing in a monorepo build.
const nextConfig: NextConfig = {};
export default nextConfig;

