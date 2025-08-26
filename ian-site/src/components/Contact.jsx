import { useState } from "react";
import { motion } from "framer-motion";

export default function Contact() {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [submitted, setSubmitted] = useState(false);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (form.name && form.email && form.message) {
      setSubmitted(true);
    }
  }

  return (
    <section id="contact" className="py-24 bg-gray-800">
      <div className="container mx-auto px-6 max-w-lg">
        <h2 className="text-3xl md:text-5xl font-display font-bold mb-8 text-center text-gold">Get in Touch</h2>
        {submitted ? (
          <p className="text-center text-yellow-400">Thank you! We'll be in touch.</p>
        ) : (
          <form onSubmit={handleSubmit} className="space-y-4">
            {['name', 'email', 'message'].map((field) => (
              <motion.div key={field} initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} viewport={{ once: true }}>
                {field !== 'message' ? (
                  <input
                    type={field === 'email' ? 'email' : 'text'}
                    name={field}
                    placeholder={field.charAt(0).toUpperCase() + field.slice(1)}
                    className="w-full p-3 rounded bg-gray-700 focus:outline-none focus:ring-2 focus:ring-yellow-500"
                    value={form[field]}
                    onChange={handleChange}
                    required
                  />
                ) : (
                  <textarea
                    name="message"
                    placeholder="Message"
                    className="w-full p-3 rounded bg-gray-700 focus:outline-none focus:ring-2 focus:ring-yellow-500 h-32"
                    value={form.message}
                    onChange={handleChange}
                    required
                  />
                )}
              </motion.div>
            ))}
            <motion.button
              type="submit"
              whileHover={{ scale: 1.05 }}
              className="w-full bg-yellow-500 text-gray-900 font-semibold py-3 rounded"
            >
              Send Message
            </motion.button>
          </form>
        )}
      </div>
    </section>
  );
}
