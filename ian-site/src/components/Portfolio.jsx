import { motion } from "framer-motion";

const works = [
  { id: 1, title: "Project One" },
  { id: 2, title: "Project Two" },
  { id: 3, title: "Project Three" },
];

export default function Portfolio() {
  return (
    <section id="portfolio" className="py-24 bg-gray-800">
      <div className="container mx-auto px-6">
        <h2 className="text-3xl md:text-5xl font-display font-bold mb-12 text-center text-gold">Featured Work</h2>
        <div className="grid md:grid-cols-3 gap-8">
          {works.map((work) => (
            <motion.div
              key={work.id}
              className="bg-gray-700 p-6 rounded-lg hover:bg-gray-600 transition-colors"
              whileHover={{ scale: 1.03 }}
            >
              <h3 className="text-xl font-semibold mb-2">{work.title}</h3>
              <p className="text-gray-300">A brief description of {work.title}.</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
