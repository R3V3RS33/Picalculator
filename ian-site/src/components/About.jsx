import { motion } from "framer-motion";
import aboutImg from "../assets/react.svg"; // placeholder image

export default function About() {
  return (
    <section id="about" className="py-24 container mx-auto px-6 grid md:grid-cols-2 gap-10 items-center">
      <motion.img
        src={aboutImg}
        alt="About"
        className="w-full max-w-md mx-auto"
        initial={{ opacity: 0, x: -50 }}
        whileInView={{ opacity: 1, x: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8 }}
      />
      <motion.div
        initial={{ opacity: 0, x: 50 }}
        whileInView={{ opacity: 1, x: 0 }}
        viewport={{ once: true }}
        transition={{ duration: 0.8 }}
      >
        <h2 className="text-3xl md:text-5xl font-display font-bold mb-4 text-gold">About Ian</h2>
        <p className="text-gray-300 leading-relaxed">
          Ian Clements is an innovator and creative force driving engaging digital
          experiences. This site showcases a selection of his work and accolades
          through a seamless interactive journey.
        </p>
      </motion.div>
    </section>
  );
}
