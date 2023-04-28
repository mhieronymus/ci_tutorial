FROM mambaorg/micromamba:latest

COPY --chown=$MAMBA_USER:$MAMBA_USER env.yaml /tmp/env.yaml
RUN micromamba install -y -n base -f /tmp/env.yaml && \
    micromamba clean --all --yes

COPY plot_scripts.py /app/
WORKDIR /app/notebooks
EXPOSE 1234
CMD ["jupyter", "lab", "--port", "1234", "--allow-root", "--no-browser", "--ip", "0.0.0.0"]