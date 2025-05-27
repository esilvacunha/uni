## Segeln Lernen – SARSA in a Windy Gridworld

**🧠 Course**: Grundlage Adaptive Wissenssysteme  
**🎯 Focus**: Reinforcement Learning using SARSA  
**📌 Main Topic**: Adaptive decision-making in dynamic environments  

---

### Project Overview  
Implemented a SARSA-based agent to navigate a gridworld lake from shore (start) to island (goal). The environment includes a **position-dependent northward wind** that affects movement and must be learned by the agent.

---

### Key Challenge  
The agent has no prior knowledge of the wind, which alters its position after each action. The goal is to learn an optimal policy despite this unknown dynamic.

---

### Tasks
- **(a)** Basic SARSA with ε=0.1, α=0.1, Q-values = 0  
- **(b)** Add diagonal and null actions; compare strategy quality  
- **(c)** Introduce stochastic wind; analyze learning performance
