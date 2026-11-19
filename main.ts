// Entry point for the gta6-meme-x-01 submission (Node 22, standard library only).
//
// The entry is the X post itself: the meme picture and its caption go out
// from a public account, and this repository hands the house the post's
// address in POST.json. All this program has to do is carry POST.json from
// the repository root into /output/POST.json, where the gate reads it.
//
// Run it locally with:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
//
// POST.json ships with a placeholder address until the post is live; the
// parent replaces it with the real https://x.com/<handle>/status/<id> URL
// before the entry is submitted.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const POST_FILE = "POST.json";

mkdirSync(OUTPUT_DIR, { recursive: true });

try {
  const target = join(OUTPUT_DIR, POST_FILE);
  copyFileSync(join(BOT_DIR, POST_FILE), target);
  const post = JSON.parse(readFileSync(target, "utf8")) as { url?: unknown };
  if (typeof post.url !== "string" || !post.url.startsWith("https://")) {
    console.error(`POST.json has no usable post URL: ${JSON.stringify(post)}`);
    process.exit(1);
  }
  console.log(`Copied ${POST_FILE} to ${target} (post: ${post.url}).`);
} catch (err) {
  console.error(`Could not copy ${POST_FILE} from ${BOT_DIR}: ${(err as Error).message}`);
  process.exit(1);
}
