import { motion } from "framer-motion";

const testimonials = [
  { id: 1, quote: "Ian's work elevated our brand.", author: "Luxury Co." },
  { id: 2, quote: "A visionary with meticulous execution.", author: "Artistic Inc." },
];

export default function Testimonials() {
  return (
    <section id="testimonials" className="py-24">
      <div className="container mx-auto px-6 text-center">
        <h2 className="text-3xl md:text-5xl font-display font-bold mb-12 text-gold">Testimonials</h2>
        <div className="flex flex-col md:flex-row gap-8 justify-center">
          {testimonials.map((t) => (
            <motion.div
              key={t.id}
              className="bg-gray-800 p-8 rounded-lg shadow-lg max-w-md"
              whileHover={{ rotateY: 10 }}
            >
              <p className="text-gray-200 italic mb-4">"{t.quote}"</p>
              <p className="text-yellow-400 font-semibold">{t.author}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
