from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .playwright_config import get_browser
from .llm_config import get_llm_client

class ReviewsAPI(View):
    def get(self, request):
        url = request.GET.get('url')
        browser = get_browser()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)

        # Use LLM to identify dynamic CSS selectors for reviews
        llm_client = get_llm_client()
        css_selectors = llm_client.identify_css_selectors(page.content())

        # Extract reviews using CSS selectors
        reviews = []
        for selector in css_selectors:
            reviews.extend(page.query_selector_all(selector))

        # Handle pagination
        next_page_url = page.query_selector('a.next')
        while next_page_url:
            page.goto(next_page_url.get_attribute('href'))
            reviews.extend(page.query_selector_all(css_selectors))

        # Extract review information
        reviews_data = []
        for review in reviews:
            title = review.query_selector('h2.review-title')
            body = review.query_selector('p.review-body')
            rating = review.query_selector('span.review-rating')
            reviewer = review.query_selector('span.reviewer-name')

            # Extract text content and handle missing elements
            title_text = title.text_content() if title else ''
            body_text = body.text_content() if body else ''
            rating_text = rating.text_content() if rating else ''
            reviewer_text = reviewer.text_content() if reviewer else ''

            # Convert rating to integer if possible
            try:
                rating_value = int(rating_text)
            except ValueError:
                rating_value = rating_text

            reviews_data.append({
                'title': title_text.strip(),  # Remove leading/trailing whitespace
                'body': body_text.strip(),  # Remove leading/trailing whitespace
                'rating': rating_value,
                'reviewer': reviewer_text.strip()  # Remove leading/trailing whitespace
            })

        # Return JsonResponse with exact format
        return JsonResponse({
            'reviews_count': len(reviews_data),
            'reviews': reviews_data
        }, json_dumps_params={'indent': 4})  # Pretty-print JSON with indentation