from .base_page import BasePage
from playwright.sync_api import Page

class MapComponent(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.map_container = '#mapcon, .leaflet-container'
        self.zoom_in_btn = '.leaflet-control-zoom-in'
        self.zoom_out_btn = '.leaflet-control-zoom-out'
        self.markers = '.leaflet-marker-icon'
        self.marker_clusters = '.marker-cluster'
        
    def zoom_in(self):
        """Zoom in on map"""
        self.click_element(self.zoom_in_btn)
        self.wait_for_timeout(500)
        
    def zoom_out(self):
        """Zoom out on map"""
        self.click_element(self.zoom_out_btn)
        self.wait_for_timeout(500)
        
    def get_marker_count(self) -> int:
        """Get number of visible markers"""
        return self.page.locator(self.markers).count()
        
    def get_cluster_count(self) -> int:
        """Get number of marker clusters"""
        return self.page.locator(self.marker_clusters).count()
        
    def click_marker(self, index: int = 0):
        """Click on a marker by index"""
        markers = self.page.locator(self.markers)
        if markers.count() > index:
            markers.nth(index).click()
            
    def click_cluster(self, index: int = 0):
        """Click on a cluster by index"""
        clusters = self.page.locator(self.marker_clusters)
        if clusters.count() > index:
            clusters.nth(index).click()
            
    def pan_map(self, x_offset: int, y_offset: int):
        """Pan map by dragging"""
        map_element = self.page.locator(self.map_container)
        map_element.drag_to(map_element, source_position={"x": 100, "y": 100}, 
                           target_position={"x": 100 + x_offset, "y": 100 + y_offset})
        
        
    def get_cluster_text(self, index: int = 0) -> str:
        """Get text from cluster marker"""
        clusters = self.page.locator(self.marker_clusters)
        if clusters.count() > index:
            return clusters.nth(index).text_content()
        return ""
