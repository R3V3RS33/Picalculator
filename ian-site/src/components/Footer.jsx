import { motion } from "framer-motion";

export default function Footer() {
  return (
    <footer className="py-6 bg-gray-900 text-center">
      <motion.p whileHover={{ scale: 1.05 }} className="text-gray-500">
        © {new Date().getFullYear()} Ian Clements. All rights reserved.
      </motion.p>
    </footer>
  );
}
