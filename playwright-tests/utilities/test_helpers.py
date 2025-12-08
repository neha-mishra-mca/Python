import time
from playwright.sync_api import Page

class TestHelpers:
    """Helper functions for test execution"""
    
    @staticmethod
    def measure_performance(func, *args, **kwargs):
        """Measure execution time of a function"""
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return result, execution_time
    
    @staticmethod
    def check_page_responsiveness(page: Page) -> bool:
        """Check if page is responsive"""
        try:
            ready_state = page.evaluate("document.readyState")
            return ready_state == "complete"
        except:
            return False
    
    @staticmethod
    def check_for_javascript_errors(page: Page) -> list:
        """Check for JavaScript errors on page"""
        errors = []
        
        def handle_console(msg):
            if msg.type == "error":
                errors.append(msg.text)
        
        page.on("console", handle_console)
        return errors
    
    @staticmethod
    def wait_for_network_idle(page: Page, timeout: int = 5000):
        """Wait for network to be idle"""
        page.wait_for_load_state("networkidle", timeout=timeout)
    
    @staticmethod
    def capture_network_requests(page: Page) -> list:
        """Capture network requests"""
        requests = []
        
        def handle_request(request):
            requests.append({
                'url': request.url,
                'method': request.method,
                'headers': request.headers
            })
        
        page.on("request", handle_request)
        return requests
    
    @staticmethod
    def simulate_slow_network(page: Page):
        """Simulate slow network conditions"""
        # Simulate slow 3G
        page.context.set_extra_http_headers({"Connection": "slow"})
    
    @staticmethod
    def check_accessibility_violations(page: Page) -> dict:
        """Basic accessibility check"""
        try:
            # Inject axe-core if available
            page.add_script_tag(url="https://unpkg.com/axe-core@4.7.0/axe.min.js")
            violations = page.evaluate("axe.run()")
            return violations
        except:
            return {"violations": []}
    
    @staticmethod
    def generate_test_report_data(test_name: str, status: str, duration: float, errors: list = None):
        """Generate test report data"""
        return {
            'test_name': test_name,
            'status': status,
            'duration': duration,
            'timestamp': time.time(),
            'errors': errors or []
        }
