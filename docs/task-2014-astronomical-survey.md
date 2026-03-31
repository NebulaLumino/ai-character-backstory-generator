# AI Agents in Astronomical Survey AI & Cataloguing

Modern astronomy generates data at a rate that has fundamentally outpaced human analysis capacity. The Vera C. Rubin Observatory (formerly LSST), when fully operational, will produce approximately 20 terabytes of imaging data per night—equivalent to the entire Hubble Space Telescope archive every few days. Each image contains millions of astronomical objects that must be identified, classified, and cross-matched against existing catalogs. The European Space Agency's Gaia mission has mapped nearly two billion stars with microarcsecond precision. The Square Kilometre Array will generate data flows exceeding the global internet traffic of the early 2000s. AI agents are not merely helpful for managing this data deluge—they are essential.

## Machine Learning in Astronomical Object Classification

The classification of astronomical objects—distinguishing stars from galaxies, identifying quasars, flagging gravitational lenses—is a textbook machine learning problem. The morphological, photometric, and spectroscopic features of astronomical objects are well-characterized, large labeled datasets exist (from previous surveys and spectroscopic follow-up), and the classification task is well-defined. Convolutional neural networks trained on galaxy images have achieved accuracy exceeding 97% on morphological classification tasks that would take human experts minutes per object.

The real power of AI in astronomical classification lies not in replicating human decisions but in discovering features that humans miss. Deep learning models trained on large galaxy image datasets have spontaneously learned to recognize features that correlate with physical properties—bars, spiral arms, tidal features—that were not explicitly labeled in training data. This emergent feature learning suggests that AI can be a tool for scientific discovery, not just automation.

## Anomaly Detection at Scale

Perhaps the most scientifically valuable application of AI in astronomical surveys is anomaly detection. The universe undoubtedly contains phenomena that have never been observed—objects that don't fit existing categories, transient events with no precedent, correlations that challenge current theory. Human experts, biased by their training and limited by attention, are poor at detecting the unexpected. AI agents, properly designed, can be tuned to flag deviations from known patterns, surfacing potentially novel phenomena for human investigation.

Novel approaches include variational autoencoders (VAEs) and generative adversarial networks (GANs) trained to model the distribution of "normal" astronomical objects. Objects that the model cannot reconstruct well—that have unexpectedly high anomaly scores—are flagged for follow-up. This approach has already led to the discovery of unusual transient events and gravitational lens candidates that had been overlooked in previous surveys.

## Cross-Matching and Database Integration

Modern astronomy is fundamentally database-driven. Every observation must be cross-matched against existing catalogs, light curves must be correlated with known variable star populations, and positional associations must be evaluated statistically. At the scale of billions of objects, these cross-matching tasks are computationally prohibitive with naive methods.

AI-based approximate nearest-neighbor search methods have dramatically accelerated cross-matching. Graph neural networks can learn the relationship between photometric and spectroscopic measurements, enabling probabilistic cross-matching that properly accounts for measurement uncertainties. This is particularly important for Time Domain astronomy—following the evolution of objects over time—which requires linking transient detections to persistent sources across vast datasets.

## Adaptive Survey Strategy

The most advanced AI agents in astronomical surveys go beyond mere data analysis to actively manage the survey itself. The Rubin's alert broker system generates alerts within 60 seconds of detection, classifying transient events and distributing them to follow-up facilities. AI agents can decide which transients warrant expensive spectroscopic follow-up, how to allocate telescope time across competing scientific priorities, and how to adapt the survey strategy in response to unexpected discoveries.

The concept of the "robotic astronomer"—an AI agent that plans, executes, and interprets its own observations—is becoming a reality. These agents must reason about scientific priorities, optimize observing schedules, handle unexpected events (weather, equipment failures), and update their models based on new data. This is AI not as a tool used by humans but as an autonomous scientific agent in its own right.

## The Path Forward: Foundation Models for Astronomy

The emergence of foundation models—large, pre-trained neural networks that can be fine-tuned for specific tasks—has transformed AI in astronomy. Models pre-trained on massive astronomical image datasets can be fine-tuned for specific classification tasks with dramatically less labeled data. This is enabling AI applications for rare object classes where labeled training data is scarce, and for wavelengths or survey datasets where manual labeling is impractical.

The goal of the astronomical community is increasingly toward AI systems that can seamlessly work across wavelengths, time domains, and physical scales—a universal astronomical assistant that can reason about objects at the scale of galaxies while also understanding the microphysics of stellar atmospheres. This will require not just better algorithms but better training data: labeled, cross-matched, multi-wavelength datasets that serve as the foundation for astronomical AI.
