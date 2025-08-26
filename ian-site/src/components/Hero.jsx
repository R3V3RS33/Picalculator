import { motion } from "framer-motion";

export default function Hero() {
  return (
    <section className="relative h-screen flex flex-col justify-center items-center text-center overflow-hidden">
      <motion.h1
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 1 }}
        className="text-5xl md:text-7xl font-display font-bold tracking-widest text-gold"
      >
        IAN CLEMENTS
      </motion.h1>
      <motion.p
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1 }}
        className="mt-4 text-lg md:text-2xl text-gray-300"
      >
        Premium digital experiences crafted with art and precision.
      </motion.p>
      <motion.a
        href="#about"
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.95 }}
        className="mt-10 px-8 py-3 bg-gold text-charcoal rounded-full font-semibold shadow-lg"
      >
        Discover More
      </motion.a>
    </section>
  );
}
