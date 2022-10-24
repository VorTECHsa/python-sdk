from tests.testcases import TestCaseUsingRealAPI
from vortexasdk.endpoints.products import Products
from vortexasdk.endpoints.products_result import DEFAULT_COLUMNS


class TestProductsReal(TestCaseUsingRealAPI):
    def test_search(self):
        products = Products().search().to_list()
        assert len(products) > 0

    def test_search_dataframe(self):
        df = Products().search().to_df()
        assert list(df.columns) == DEFAULT_COLUMNS
        assert len(df) > 0

    def test_search_dataframe_subset_of_cols(self):
        df = Products().search().to_df(columns=["name", "id"])
        assert list(df.columns) == ["name", "id"]
        assert len(df) > 0

    def test_search_exact_match(self):
        search_term = "Gasoil"

        # Confirm that searching our search term does indeed yield more than one result
        products = Products().search(search_term).to_list()
        if len(products) <= 1:
            raise Exception(
                f"Unable to perform exact match test on {search_term}."
            )

        products_exact = (
            Products().search(search_term, exact_term_match=True).to_list()
        )

        assert {p.name for p in products_exact} == {search_term}

    def test_load_all(self):
        all_products = Products().load_all()

        assert len(all_products) > 20

    def test_search_multiple_terms_to_dataframe(self):
        df = (
            Products()
            .search(
                term=["diesel", "fuel oil", "grane", "lng", "lpg", "crude"]
            )
            .to_df("all")
        )

        expected_columns = {
            "id",
            "name",
            "layer.0",
            "leaf",
            "parent.0.name",
            "parent.0.layer.0",
            "parent.0.id",
            "meta.api_min",
            "meta.api_max",
            "ref_type",
            "meta.sulphur_min",
            "meta.sulphur_max",
        }

        assert expected_columns.issubset(set(df.columns))

    def test_search_with_filter_layer(self):
        prodType = "group_product"
        df = Products().search(filter_layer=prodType).to_df()

        assert list(df["layer.0"].unique()) == [prodType]
