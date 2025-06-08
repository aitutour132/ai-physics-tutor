import streamlit as st
import openai

# Initialize OpenAI key
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("AI Physics Tutor — Text + Images")

# User input
question = st.text_input("Ask a physics question or topic:")

if st.button("Explain"):
    if question:
        # Call GPT to generate text explanation
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful physics tutor."},
                {"role": "user", "content": f"Explain this physics topic in simple steps: {question}"}
            ],
            max_tokens=500,
            temperature=0.7,
        )
        explanation = response.choices[0].message.content
        st.write(explanation)

        # Generate image prompt based on question
        image_prompt = f"Simple line drawing diagram illustrating {question} for physics students"
        st.write(f"**Diagram prompt:** {image_prompt}")

        # Placeholder for image generation
        st.image("https://via.placeholder.com/400x300.png?text=Diagram+will+go+here")

