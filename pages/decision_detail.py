from pages.base import Base


class DecisionDetail(Base):
    """
    Decision Page covering the generic methods for all Decision statuses
    (Discussion, Proposal, Decision, Archived)
    """

    def __init__(self, driver):
        self.driver = driver
        # Check we're in a detail view
        with self.assert_element_visible():
            driver.find_element_by_id("decision_snippet_envelope")

    def edit_description(self):
        edit_link = self.driver.find_element_by_css_selector(".controls > .edit")
        edit_link.click()
