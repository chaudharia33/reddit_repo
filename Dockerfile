# Copy app configuration
COPY .env_api /.env_api  

# Copy app code
COPY app/ /app/

# Add PATH and PYTHONPATH to avoid issues w/ python modules
ENV PATH="$PATH:/"
ENV PYTHONPATH="$PYTHONPATH:/"

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]