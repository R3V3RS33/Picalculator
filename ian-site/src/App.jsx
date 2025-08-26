import Hero from "./components/Hero";
import About from "./components/About";
import Portfolio from "./components/Portfolio";
import Testimonials from "./components/Testimonials";
import Contact from "./components/Contact";
import Footer from "./components/Footer";

export default function App() {
  return (
    <main className="font-sans">
      <Hero />
      <About />
      <Portfolio />
      <Testimonials />
      <Contact />
      <Footer />
    </main>
  );
}
